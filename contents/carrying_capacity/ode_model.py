import scipy.integrate


# Fixed r Model (Exponential Growth)
def exp_growth_model(t, N, r):
    dNdt = r * N
    return dNdt


# Fixed r, K Model
def carrying_capacity_model(t, N, r, K):
    dNdt = r * N - r / K * N ** 2
    return dNdt


def fixed_daily_nu_model(t, N, dN):
    return dN


def fixed_daily_nu_and_fixed_retention_model(t, N, dN, ret):
    dNdt = dN - (1 - ret) * N
    return dNdt


def solve_model(model, t_seq, n_0, *args):
    sol = scipy.integrate.solve_ivp(
        model,
        t_span=(t_seq[0], t_seq[-1]),
        y0=[n_0],
        args=args,
        t_eval=t_seq
    )

    return sol