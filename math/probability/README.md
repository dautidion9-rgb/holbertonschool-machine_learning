# Probability

Implementations of four classic probability distributions in pure Python —
no imported modules, not even `math`. Each distribution is a class that can
either be initialized with known parameters or estimate its parameters from
a list of data.

Part of the Holberton School machine learning curriculum.

## Distributions

| File | Class | Parameters | Methods |
| ---- | ----- | ---------- | ------- |
| `poisson.py` | `Poisson` | `lambtha` | `pmf(k)`, `cdf(k)` |
| `exponential.py` | `Exponential` | `lambtha` | `pdf(x)`, `cdf(x)` |
| `normal.py` | `Normal` | `mean`, `stddev` | `z_score(x)`, `x_value(z)`, `pdf(x)`, `cdf(x)` |
| `binomial.py` | `Binomial` | `n`, `p` | `pmf(k)`, `cdf(k)` |

## Usage

Every class follows the same pattern: pass a list of data to estimate the
parameters, or set them directly.

```python
#!/usr/bin/env python3
Normal = __import__('normal').Normal

# Estimate mean and stddev from data
n1 = Normal(data=[68.2, 71.5, 69.8, 72.1, 70.3])
print(n1.mean, n1.stddev)

# Or set the parameters directly
n2 = Normal(mean=70, stddev=10)
print(n2.pdf(90))   # probability density at x = 90
print(n2.cdf(90))   # probability that X <= 90
```

Invalid input raises the appropriate exception: a `TypeError` if `data` is
not a list, and a `ValueError` for fewer than two data points or for
non-positive parameters.

## Implementation notes

- Since nothing can be imported, the constants `e = 2.7182818285` and
  `pi = 3.1415926536` are hardcoded, and factorials are computed with loops.
- The normal CDF uses a Taylor series approximation of the error function.
- The binomial constructor estimates `n` and `p` from data using the method
  of moments: `p` is computed first, `n` is rounded to the nearest integer,
  then `p` is recalculated so the two stay consistent.

## Requirements

- Python 3 (`#!/usr/bin/env python3`)
- No imported modules
- `pycodestyle` compliant
- All modules, classes, and functions are documented
