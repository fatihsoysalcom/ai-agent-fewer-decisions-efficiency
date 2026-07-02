import time

# --- Agent Tools (Simulated Functions) ---
def sum_numbers(nums):
    """Tool: Calculates the sum of a list of numbers."""
    return sum(nums)

def product_numbers(nums):
    """Tool: Calculates the product of a list of numbers. Handles empty lists by returning 1."""
    product = 1
    for n in nums:
        product *= n
    return product

def filter_positive(nums):
    """Tool: Filters out positive numbers (greater than 0)."""
    return [n for n in nums if n > 0]

def filter_negative(nums):
    """Tool: Filters out negative numbers (less than 0)."""
    return [n for n in nums if n < 0]

# --- Agent 1: Simulating More Decisions / Less Optimized Strategy ---
class AgentWithManyDecisions:
    def __init__(self, name="Agent Alpha"):
        self.name = name
        self.decision_count = 0

    def process_data(self, data):
        print(f"\n--- {self.name} (More Decisions Strategy) Processing ---")
        self.decision_count = 0
        start_time = time.perf_counter()

        # Decision 1: Agent considers a general sum, even if not directly needed for the goal.
        self.decision_count += 1 # Illustrates a decision point
        # print(f"  Decision {self.decision_count}: Considering summing all numbers (general approach).")
        # total_sum_attempt = sum_numbers(data) # This might be computed and then discarded by a less efficient agent.

        # Decision 2: Agent decides to filter for positive numbers to meet a specific part of the goal.
        self.decision_count += 1 # Illustrates a decision point
        # print(f"  Decision {self.decision_count}: Filtering positive numbers for specific sum.")
        positives = filter_positive(data)

        # Decision 3: Agent decides to apply the sum tool to the filtered positive numbers.
        self.decision_count += 1 # Illustrates a decision point
        # print(f"  Decision {self.decision_count}: Summing positive numbers.")
        sum_of_positives = sum_numbers(positives)

        # Decision 4: Agent considers a general product, another potentially redundant step.
        self.decision_count += 1 # Illustrates a decision point
        # print(f"  Decision {self.decision_count}: Considering producting all numbers (general approach).")
        # total_product_attempt = product_numbers(data) # Another potentially discarded computation.

        # Decision 5: Agent decides to filter for negative numbers to meet another specific part of the goal.
        self.decision_count += 1 # Illustrates a decision point
        # print(f"  Decision {self.decision_count}: Filtering negative numbers for specific product.")
        negatives = filter_negative(data)

        # Decision 6: Agent decides to apply the product tool to the filtered negative numbers.
        self.decision_count += 1 # Illustrates a decision point
        # print(f"  Decision {self.decision_count}: Producting negative numbers.")
        product_of_negatives = product_numbers(negatives)

        end_time = time.perf_counter()
        duration = (end_time - start_time) * 1000 # milliseconds

        print(f"  Sum of positives: {sum_of_positives}")
        print(f"  Product of negatives: {product_of_negatives}")
        print(f"  Total simulated decision points: {self.decision_count}") # Key metric from the article
        print(f"  Time taken: {duration:.2f} ms")
        return sum_of_positives, product_of_negatives

# --- Agent 2: Simulating Fewer Decisions / Optimized Strategy ---
class AgentWithFewerDecisions:
    def __init__(self, name="Agent Beta"):
        self.name = name
        self.decision_count = 0

    def process_data(self, data):
        print(f"\n--- {self.name} (Fewer Decisions Strategy) Processing ---")
        self.decision_count = 0
        start_time = time.perf_counter()

        # Decision 1 (Strategic): Agent makes an initial, overarching decision to categorize data
        # based on the ultimate goals (sum positives, product negatives). This single decision
        # streamlines subsequent operations, reducing the need for many sequential decisions.
        self.decision_count += 1 # Illustrates a strategic decision point
        # print(f"  Decision {self.decision_count}: Strategically categorizing data for specific goals.")
        positives = filter_positive(data)
        negatives = filter_negative(data)

        # Decision 2: Agent directly applies the sum tool to the already categorized positive numbers.
        self.decision_count += 1 # Illustrates a decision point
        # print(f"  Decision {self.decision_count}: Summing positive numbers.")
        sum_of_positives = sum_numbers(positives)

        # Decision 3: Agent directly applies the product tool to the already categorized negative numbers.
        self.decision_count += 1 # Illustrates a decision point
        # print(f"  Decision {self.decision_count}: Producting negative numbers.")
        product_of_negatives = product_numbers(negatives)

        end_time = time.perf_counter()
        duration = (end_time - start_time) * 1000 # milliseconds

        print(f"  Sum of positives: {sum_of_positives}")
        print(f"  Product of negatives: {product_of_negatives}")
        print(f"  Total simulated decision points: {self.decision_count}") # Key metric from the article
        print(f"  Time taken: {duration:.2f} ms")
        return sum_of_positives, product_of_negatives

# --- Main Execution ---
if __name__ == "__main__":
    sample_data = [-5, 10, -2, 7, 0, 15, -3, 8]
    print(f"Initial Input Data: {sample_data}")

    # Run Agent with More Decisions Strategy
    agent_alpha = AgentWithManyDecisions()
    agent_alpha.process_data(sample_data)

    # Run Agent with Fewer Decisions Strategy
    agent_beta = AgentWithFewerDecisions()
    agent_beta.process_data(sample_data)

    # Example with a larger dataset to better illustrate potential time differences
    large_data = [i if i % 2 == 0 else -i for i in range(-10000, 10001)]
    print(f"\n--- Processing Larger Dataset ({len(large_data)} items) ---")
    agent_alpha.process_data(large_data)
    agent_beta.process_data(large_data)
