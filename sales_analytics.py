
def total_revenue(sales):
    return sum(sales)


def average_revenue(sales):
    if not sales:
        return 0

    return total_revenue(sales) / len(sales)


def highest_revenue(sales):
    if not sales:
        return None

    return max(sales)


def count_above_average(sales):
    if not sales:
        return 0

    average = average_revenue(sales)

    return sum(1 for value in sales if value > average)


def revenue_summary(sales):
    if not sales:
        return {
            "total_revenue": 0,
            "average_revenue": 0,
            "highest_revenue": None,
            "count_above_average": 0
        }

    total = total_revenue(sales)
    average = total / len(sales)
    highest = max(sales)
    count = sum(1 for value in sales if value > average)

    return {
        "total_revenue": total,
        "average_revenue": average,
        "highest_revenue": highest,
        "count_above_average": count
    }
