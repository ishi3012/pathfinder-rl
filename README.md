# Cliff Walking Policy Iteration

This repository contains the implementation of fixed policies and policy iteration for solving the Cliff Walking problem, as described in Sutton & Barto's *Reinforcement Learning: An Introduction* (2nd Edition, Chapter 4). The goal of this project is to compare the performance of fixed policies and derive an optimal policy using the Policy Iteration algorithm.

## Repository Structure

```
cliff-walking-policy-iteration/
├── README.md                # This file
├── requirements.txt         # Project dependencies
├── main.py                  # Main script to run the experiments
├── environment.py           # Environment setup and exploration
├── utils.py                 # Helper functions (policy generation, run logic, etc.)
├── results/                 # Folder to store outputs like histograms and results
└── LICENSE                  # [MIT License](./LICENSE)
```

## Assignment Overview

### Part 1: Fixed Policies

Your task for this part is to try a few other policies and compare their performances. Follow these steps:

1. **Try 3 Fixed Policies**: Implement three different fixed policies, each with a unique random seed (except for seed=17).

   - Each policy should be evaluated under the same environment conditions.

2. **Experimentation**: For each policy:

   - Run the experiment 100 times (i.e., 100 runs).
   - Store the results for analysis.

3. **Performance Metrics**:

   - Compute and report the mean and standard deviation (stdev) of the total number of steps over 100 runs.
   - Select the BEST policy based on the total number of steps.

4. **Visualization**:

   - Display the selected policy in a 2D array format.
   - Generate a histogram showing:
     - Number of steps taken.
     - Ratio of near-falls.
     - Rewards.

   Below is an example histogram generated for the first policy (seed=17):

   *(Insert example histogram here)*

---

### Part 2: Optimal Policy by Policy Iteration

Your task for this part is to implement the Policy Iteration algorithm to derive the optimal policy for the Cliff Walking environment. Follow these steps:

1. **Algorithm Implementation**:

   - Implement the Policy Iteration algorithm as described in Sutton & Barto (2nd Edition, Chapter 4.3, Page 80).
   - Ensure the iteration terminates when the policy becomes stable (approximating the optimal policy).

2. **Deliverables**:

   - Provide the implementation in `main.py` and necessary helpers in `utils.py`.
   - Output the derived optimal policy in a 2D array format.
   - Generate visualizations (e.g., heatmaps or histograms) to demonstrate the effectiveness of the optimal policy.

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/cliff-walking-policy-iteration.git
   cd cliff-walking-policy-iteration
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. To run experiments for fixed policies:

   ```bash
   python main.py --fixed_policy
   ```

2. To run the policy iteration algorithm:

   ```bash
   python main.py --optimal_policy
   ```

---

## Results

Results will be stored in the `results/` directory, including:

- Histograms for fixed policies.
- 2D array representations of the best fixed policy and the optimal policy.

---

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for more details.

