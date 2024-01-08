import argparse

import numpy as np

np.random.seed(1)


def f1(x: np.ndarray):
    return np.sqrt(1 - x * x)


def f2(x: np.ndarray):
    x1 = x[:, 0]
    x2 = x[:, 1]

    y = x1 * x1 + x2 * x2
    return (y < 1.0).astype(np.double)


def get_expectation_and_std(x: np.ndarray, func):
    N = x.shape[0]

    y = func(x)

    mu = np.sum(y) / N * 4.0
    sigma = np.sqrt(np.sum((y - mu) ** 2)) / N

    return (mu, sigma)


def main():
    parse = argparse.ArgumentParser()

    parse.add_argument(
        "-n",
        type=int,
        default=1000000,
        help="generate n samples",
    )

    args = parse.parse_args()

    N = args.n

    assert N % 2 == 0

    x = np.random.rand(N)
    xpack = x.reshape(N // 2, 2)

    mu1, sigma1 = get_expectation_and_std(x, f1)
    mu2, sigma2 = get_expectation_and_std(xpack, f2)

    print(f"f1: {mu1}, {sigma1}")
    print(f"f2: {mu2}, {sigma2}")


if __name__ == "__main__":
    main()
