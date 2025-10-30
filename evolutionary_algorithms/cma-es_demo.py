'''
Given:
  f(x)         → objective function to minimize
  n            → number of parameters (dimension of x)
  m0           → initial mean vector
  σ0           → initial global step size
  λ            → population size (number of offspring per generation)
  μ            → number of best samples used for update
  w_i          → recombination weights (larger for better samples)

Initialize:
  m ← m0                        # initial mean
  σ ← σ0                        # global step size
  C ← I_n                       # covariance matrix (identity)
  p_c ← 0_n                     # evolution path for covariance
  p_σ ← 0_n                     # evolution path for step size
  set strategy parameters: c_c, c_σ, c_1, c_μ, d_σ  # learning rates

Repeat until convergence:

  # 1. SAMPLE new candidates from current distribution
  for i = 1 to λ:
      z_i ~ N(0, I_n)                        # draw from standard normal
      y_i ← B * D * z_i                      # transform by C^(1/2)
      x_i ← m + σ * y_i                      # map to search space

  # 2. EVALUATE each candidate
  for i = 1 to λ:
      f_i ← f(x_i)

  # 3. SORT candidates by fitness (ascending order)
  reorder x_i, y_i, f_i so that f_1 ≤ f_2 ≤ ... ≤ f_λ

  # 4. UPDATE the mean of the distribution (move toward good solutions)
  y_w ← Σ_{i=1}^{μ} w_i * y_i                # weighted average of good steps
  m ← m + σ * y_w                            # shift mean in direction of progress

  # 5. UPDATE evolution path for σ (cumulative path in isotropic space)
  p_σ ← (1 - c_σ) * p_σ + sqrt(c_σ * (2 - c_σ) * μ_eff) * (C^(-1/2) * y_w)

  # 6. ADAPT step size σ
  σ ← σ * exp( (c_σ / d_σ) * (||p_σ|| / E||N(0,I)|| - 1) )

  # 7. UPDATE evolution path for covariance (directional memory)
  h_σ ← 1 if ||p_σ|| / expected_norm < (1.4 + 2/(n + 1)) else 0
  p_c ← (1 - c_c)*p_c + h_σ * sqrt(c_c*(2 - c_c)*μ_eff) * y_w

  # 8. UPDATE covariance matrix (learn search shape)
  C ← (1 - c_1 - c_μ)*C
       + c_1 * (p_c * p_cᵀ)                           # rank-one update
       + c_μ * Σ_{i=1}^{μ} w_i * (y_i * y_iᵀ)         # rank-μ update

  # (Optionally) recompute eigendecomposition C = B * D² * Bᵀ every few gens

Until:
  stopping criterion met (e.g. σ < ε, f change small, or max iterations)
'''