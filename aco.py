import pandas as pd
import numpy as np

class AntColonyOptimization:
    def __init__(self, data, num_ants=20, num_iterations=50, evaporation_rate=0.5):
        self.data = data
        self.prices = data["ticket_price"].values
        self.customers = data["number_of_person"].values
        self.revenue = self.prices * self.customers

        self.num_ants = num_ants
        self.num_iterations = num_iterations
        self.evaporation_rate = evaporation_rate

        self.num_prices = len(self.prices)
        self.pheromone = np.ones(self.num_prices)

        self.best_price = None
        self.best_revenue = 0
        self.convergence = []

    def run(self):
        for iteration in range(self.num_iterations):
            all_solutions = []
            all_revenues = []

            probabilities = self.pheromone / self.pheromone.sum()

            for ant in range(self.num_ants):
                index = np.random.choice(range(self.num_prices), p=probabilities)

                price = self.prices[index]
                customer = self.customers[index]
                revenue = price * customer

                all_solutions.append(index)
                all_revenues.append(revenue)

                if revenue > self.best_revenue:
                    self.best_revenue = revenue
                    self.best_price = price

            # Evaporation
            self.pheromone = (1 - self.evaporation_rate) * self.pheromone

            # Update pheromone
            for i in range(self.num_ants):
                self.pheromone[all_solutions[i]] += all_revenues[i] / max(self.revenue)

            self.convergence.append(self.best_revenue)

        return self.best_price, self.best_revenue, self.convergence


if __name__ == "__main__":
    data = pd.read_csv("cinema_ticket_pricing_clean.csv")
    aco = AntColonyOptimization(data)
    price, revenue, curve = aco.run()

    print("Optimal Ticket Price: RM", price)
    print("Maximum Revenue: RM", revenue)
