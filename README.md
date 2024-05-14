# Investigating the Impact of Geographical Position of Nests and Noise in Decision-Making of Ants

## Description

This project investigates the impact of the geographical position of nests and noise in decision-making on the nest selection process of ants (Temnothorax albipennis). By using Monte Carlo-based simulation modeling, we explore how ants utilize a quality-dependent threshold rule to make collective decisions. The project introduces geographically varied options and noise in the values of nest qualities and decision thresholds. Additionally, the study examines whether a quorum threshold can help ants make better choices in noisy environments.

## Installation

To run this project, ensure you have the following dependencies installed:

- Python 3.x
- NumPy
- Matplotlib

You can install the required packages using pip:

```bash
pip install numpy matplotlib
```

## Usage

To use this project, follow these steps:

1. Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/your-repo-name.git
```

2. Navigate to the project directory:

```bash
cd your-repo-name
```

3. Extract the contents of `Relevant Codes and Figures.zip` to the project directory.

4. Run the Python scripts:

- For the main simulation:
  ```bash
  python ExampleUsingRobinsonCode4Nests_func.py
  ```

- To add quorum to the model, uncomment the relevant lines in `RobinsonCode.py` and run:
  ```bash
  python RobinsonCode.py
  ```

## Project Structure

- `ExampleUsingRobinsonCode4Nests_func.py`: Main script to run the simulation with geographical variation and noise in nest qualities and thresholds.
- `RobinsonCode.py`: Contains functions and classes used in the simulation. Uncomment relevant lines to include quorum threshold in the model.

## Features

### Simulation Scenarios

- **Geographical Variation**: Simulates nest selection with nests positioned at varying distances from the original nest.
- **Noise in Nest Qualities and Thresholds**: Introduces noise to investigate its impact on the decision-making process.
- **Quorum Threshold**: Examines whether a quorum threshold can mitigate the effects of noise and improve decision-making.

### Metrics

- **Nest Choice Frequency**: Tracks the frequency of each nest being chosen by the ants.
- **Discovery Time**: Measures the time taken for ants to discover and commit to a new nest.

## Results

The project compares the outcomes of simulations under different scenarios, highlighting how geographical position, noise in nest qualities, and decision thresholds affect the nest selection process. The effectiveness of adding a quorum threshold to improve decision-making in noisy environments is also evaluated.

## Contributing

If you would like to contribute to this project, please follow these guidelines:

1. Fork the repository.
2. Create a new branch with a descriptive name.
3. Make your changes and commit them with clear and concise messages.
4. Push your changes to your forked repository.
5. Create a pull request detailing the changes you have made.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

For questions or inquiries, please contact me at saqib.majumder01@gmail.com.
