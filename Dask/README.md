
# Dask + XGBoost Example

This project demonstrates how to use **Dask** for scalable, distributed machine learning with **XGBoost** on a local machine.

## 🚀 What This Project Does

- Sets up a local Dask cluster
- Generates synthetic classification data using `dask-ml`
- Trains a distributed XGBoost model on that data using Dask
- Monitors computation with the Dask dashboard
  

## ❓ What is Dask?
Dask is a flexible parallel computing library for analytics that scales from a single laptop to a large cluster. It provides advanced parallelism for analytics, enabling performance at scale for tools you already use:  

Familiar API: Dask mirrors the APIs of NumPy, pandas, and scikit-learn, so it's easy to switch from single-machine to distributed computing.  

Flexible and Scalable: Use it on your local machine, in the cloud, or on HPC systems.  

Efficient Scheduling: Dask schedules work dynamically and efficiently across multiple cores or workers.  

Interactive Dashboard: Real-time diagnostics and performance tracking via a built-in web UI (localhost:8787).    

Use Dask when your data is too big to fit in memory, or when you want to speed up computations using multiple cores or machines — all while writing Python code that looks and feels familiar.



## 📦 Requirements

Install the necessary dependencies via pip:

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install xgboost dask[complete] dask-ml
```

## 🧠 How to Run

Make sure your main Python file uses the correct multiprocessing idiom (required on Windows):

```python
if __name__ == "__main__":
    main()
```

Then run the script:

```bash
python main.py
```

## 📉 Monitoring

After the Dask cluster starts, you can open the dashboard in your browser:

```
http://localhost:8787
```

This gives you live insights into:

- Worker memory usage
- Task progress and scheduling
- CPU and I/O activity
- Execution time

## 🧪 Example Output

```
[0.8732, 0.6541, 0.9214, ...]  # First few predictions
```

## 📚 References

- [Dask Documentation](https://docs.dask.org/)
- [XGBoost with Dask](https://xgboost.readthedocs.io/en/latest/dask.html)
- [dask-ml](https://ml.dask.org/)

---

Happy scaling!
