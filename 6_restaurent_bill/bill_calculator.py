# Restaurant Bill Calculator with Discounts and Fees

MENU = {
    "paneer tikka": 250,
    "butter chicken": 240,
    "masala dosa": 200
}

LUNCH_DISCOUNT = 0.15
VOUCHER_DISCOUNT = 0.10
CARD_SERVICE_CHARGE = 0.05


def get_base_cost(dish):
    """Get the base cost of a dish from the menu."""
    if dish not in MENU:
        raise ValueError("Invalid dish selected")
    return MENU[dish]


def apply_discounts(cost, hour, has_voucher):
    """Apply time-based and voucher discounts to the cost."""
    if 12 <= hour < 15: 
        cost *= (1 - LUNCH_DISCOUNT)
    
    if has_voucher:
        cost *= (1 - VOUCHER_DISCOUNT)
    
    return cost


def apply_service_charge(cost, card_payment):
    """Apply service charge for card payments."""
    if card_payment:
        cost += cost * CARD_SERVICE_CHARGE
    return cost


def main():
    dish_names = ", ".join(MENU.keys())
    dish = input(f"Enter main dish ({dish_names}): ").strip().lower()
    
    try:
        cost = get_base_cost(dish)
    except ValueError as e:
        print(f"Error: {e}")
        return
    
    try:
        hour = int(input("Enter hour (0-23): "))
        
        if not 0 <= hour <= 23:
            raise ValueError("Invalid hour")
        
        has_voucher = input("Voucher? (yes/no): ").strip().lower() == "yes"
        card_payment = input("Card payment? (yes/no): ").strip().lower() == "yes"
        
        cost = apply_discounts(cost, hour, has_voucher)
        cost = apply_service_charge(cost, card_payment)
        
        print(f"\nFinal Bill Amount: ₹{cost:.2f}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()