import numpy as np

class ACO:
    def __init__(self, n_ants=20, n_iterations=50,
                 alpha=1, beta=2, evaporation=0.5):
        
        self.n_ants = n_ants
        self.n_iterations = n_iterations
        self.alpha = alpha
        self.beta = beta
        self.evaporation = evaporation
        
        self.price_range = np.arange(10, 31)  # RM10–RM30
        self.pheromone = np.ones(len(self.price_range))

    def demand(self, price):
        return max(0, 200 - 5 * price)

    def revenue(self, price):
        return price * self.demand(price)

    def run(self):
        best_price = None
        best_revenue = -np.inf
        history = []

        for iteration in range(self.n_iterations):
            revenues = []
            prices = []

            for _ in range(self.n_ants):
                prob = (self.pheromone ** self.alpha) * \
                       (1 / (self.price_range + 1)) ** self.beta
                prob /= prob.sum()

                idx = np.random.choice(len(self.price_range), p=prob)
                price = self.price_range[idx]

                rev = self.revenue(price)
                prices.append(idx)
                revenues.append(rev)

                if rev > best_revenue:
                    best_revenue = rev
                    best_price = price

            # Evaporation
            self.pheromone *= (1 - self.evaporation)

            # Update pheromone
            for i, rev in zip(prices, revenues):
                self.pheromone[i] += rev / 1000

            history.append(best_revenue)

        return best_price, best_revenue, history
