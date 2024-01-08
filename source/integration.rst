Monte Carlo Integration
*************************

Simple Monte Carlo Integration
=====================================

The expectation of a random variable :math:`Y` is :math:`\mu = \E(Y)`.
Then we can generate values :math:`Y_1,\ldots,Y_n` independently and randomly
from the distribution of :math:`Y` and the estimate of :math:`\mu` is

.. math::

    \hat{\mu}_n = \frac{1}{n}\sum_{i=1}^{n} Y_i \,.

Assume :math:`Y = f(X)` where random variable :math:`X\in D \subseteq \R^d`
and :math:`X` has a probability density function :math:`p(\mathbf{x})`. Then

.. math::

    \mu = \int_D f(\x) p(\x) d \x \,.


Connection to Riemann Integration
--------------------------------------

Suppose the volume of :math:`D` is :math:`V`, then

.. math::

    V = \int_D d\x \,.

If we set :math:`p(x) = 1/V`, then

.. math::

    \begin{align}
    \mu &= \int_D f(\x) p(\x) d\x \nonumber \\
        &= \frac{1}{V} \int_D f(\x) d\x \nonumber \,.
    \end{align}


Therefore,

.. math::

    \int_D f(\x) d\x = V \E(f(X)) = V \, \mu \,.

The discrete formula is

.. math::

    \begin{align}
    \int_D f(\x) d\x &\approx \sum_{i=1}^n f(x_i) \frac{V}{n} \nonumber \\
                     &= \frac{V}{n} \sum_{i=1}^n f(x_i) \nonumber \\
                     &= V \left(\frac{1}{n} \sum_{i=1}^n Y_i \right) \nonumber \\
                     &= V \mu_n \nonumber \,.
    \end{align}

According to the law of large number, :math:`\lim \limits_{n \to \infty} \hat{\mu}_n\to\mu`.


Mathematical Constant :math:`\pi`
-----------------------------------

.. literalinclude:: ../codes/pi.py
    :language: python
