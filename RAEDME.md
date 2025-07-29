# 🎲 Understanding Probability with Python

This repository explores the fundamentals of **probability** through simple, simulation-based mini-projects using Python. Probability is the measure of how likely an event is to occur, and it's a foundational concept in statistics, data science, and real-world decision making.

Through code-based experiments, this project demonstrates how random events behave, how we can calculate their likelihood, and how experimental probability converges toward theoretical values with more data.

## 📘 Topics in Probability Covered

- **Sample Space**: The set of all possible outcomes of a random experiment  
- **Events**: A subset of the sample space (e.g., getting exactly 2 heads in 3 tosses)  
- **Theoretical Probability**: Expected probability calculated by formula  
- **Experimental Probability**: Estimated from running simulations  
- **Law of Large Numbers**: As the number of trials increases, the experimental probability approaches the theoretical one  
- **Real-World Application**: Predicting rain based on historical weather data

## 📂 What This Repository Contains

| File Name                         | Description |
|-----------------------------------|-------------|
| `coin_toss_events.py`            | Simulates tossing multiple coins and filters outcomes (e.g., exactly 2 heads). |
| `dice_roll_probability.py`       | Simulates rolling dice and calculates probability of a specific outcome like rolling a 6. |
| `law_of_large_numbers.py`        | Demonstrates how probability of heads converges to 0.5 using graphs. |
| `sample_space.py`                | Generates sample spaces for 2-coin tosses, 2-dice rolls, and combined events. |
| `head_probability_estimation.py` | Runs large-scale simulation (e.g., 1 million tosses) to estimate P(Head). |
| `predict_rain_probability.ipynb` | Uses past 100 years' weather data to predict rain on a specific date using probability. |

## 🚀 How to Run

### ▶ Python Scripts
```bash
python filename.py
```

### 📓 Jupyter Notebook
- Open `predict_rain_probability.ipynb` with Jupyter Notebook or VS Code.

## 📦 Requirements

These projects use only basic Python libraries:

- `random`
- `matplotlib` (only for plotting in `law_of_large_numbers.py`)
- `jupyter` (for opening the notebook)

To install missing packages:
```bash
pip install matplotlib notebook
```

## 📌 Key Learnings

- Simulate real-world random events like coins and dice  
- Generate and analyze sample spaces  
- Observe how experimental probability behaves with more trials  
- Apply probability to real-world prediction (weather forecast)

## 📁 Suggested Folder Structure

```
probability-simulations/
├── coin_toss_events.py
├── dice_roll_probability.py
├── head_probability_estimation.py
├── law_of_large_numbers.py
├── sample_space.py
├── predict_rain_probability.ipynb
└── README.md
```

## 📬 Contact

If you're a learner, educator, or just curious — feel free to explore or connect.  
Thanks for checking it out! 🚀  
🔗 Connect with me on [LinkedIn](https://www.linkedin.com/in/digambar-baditya-b522b12a5/)
