def robustness_score(return_pct, drawdown, consistency):

    score = (
        (return_pct * 0.4) +
        ((100 - drawdown) * 0.4) +
        (consistency * 0.2)
    )

    return round(score, 2)


score = robustness_score(
    return_pct=85,
    drawdown=15,
    consistency=90
)

print("Robustness Score:", score)