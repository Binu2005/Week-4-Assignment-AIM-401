
# Lesson 4 Individual Assignment
# Digital Banking Transaction Audit Tool


# Task 1A: Clean invalid transactions using filter() and lambda
def clean_transactions(amounts, min_threshold=10.0):
    """
    Remove non-positive transactions and amounts below
    the minimum threshold.
    """
    return list(
        filter(
            lambda amount: amount > 0 and amount >= min_threshold,
            amounts
        )
    )


# Task 1B: Apply service fees using map() and lambda
def apply_service_fee(amounts, fee_rate=0.02):
    """
    Deduct a percentage service fee from every transaction.
    Return the processed amounts as a list.
    """
    return list(
        map(
            lambda amount: round(amount * (1 - fee_rate), 2),
            amounts
        )
    )


# Task 2: Calculate the total using pure recursion
def calculate_nested_total(data):
    """
    Calculate the total of a number or arbitrarily nested lists.
    Do not use loops or global variables in this function.
    """

    # Base case 1: An empty list has a total of zero.
    if isinstance(data, list) and len(data) == 0:
        return 0.0

    # Base case 2: A single integer or float.
    if isinstance(data, (int, float)):
        return float(data)

    # Recursive step: Divide the list into head and tail.
    if isinstance(data, list):
        head = data[0]
        tail = data[1:]

        return (
            calculate_nested_total(head)
            + calculate_nested_total(tail)
        )

    # Reject unsupported input types.
    raise TypeError(
        "Input must contain only integers, floats, and nested lists."
    )


# Main program: Demonstrate the audit tool
def main():

    # Sample transaction batch
    transactions = [
        150.00, 8.00, -20.00, 500.00,
        25.00, 0.00, 75.50, 10.00
    ]

    # Step 1: Clean the transaction amounts.
    valid_transactions = clean_transactions(transactions)

    # Step 2: Deduct the 2% service fee.
    processed_transactions = apply_service_fee(valid_transactions)

    # Step 3: Calculate the nested transaction total.
    nested_transactions = [
        100,
        [50, 25],
        [[10, 5], 40]
    ]

    nested_total = calculate_nested_total(nested_transactions)

    # Display the results.
    print("=" * 50)
    print("DIGITAL BANKING TRANSACTION AUDIT")
    print("=" * 50)

    print("\n1. ORIGINAL TRANSACTIONS")
    print(transactions)

    print("\n2. CLEANED TRANSACTIONS")
    print(valid_transactions)

    print("\n3. TRANSACTIONS AFTER 2% SERVICE FEE")
    print(processed_transactions)

    print("\n4. NESTED TRANSACTION DATA")
    print(nested_transactions)

    print(f"\n5. TOTAL NESTED TRANSACTION VALUE: ${nested_total:.2f}")

    print("\n6. AUDIT SUMMARY")
    print("-" * 50)
    print("Original transaction count:", len(transactions))
    print("Valid transaction count:", len(valid_transactions))
    print(
        "Total after service fees: "
        f"${sum(processed_transactions):.2f}"
    )

    print("\nAudit completed successfully.")


if __name__ == "__main__":
    main()
