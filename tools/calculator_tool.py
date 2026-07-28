from langchain_core.tools import tool

@tool
def calculate_park_fee(num_adults: int, num_children: int, vehicle_type: str, is_foreign: bool = False, apply_vat: bool = True) -> str:
    """
    Calculates the total park entry fee including adult fees, child fees, vehicle charges, and VAT.
    Use this tool whenever fee calculations, tax calculations, or park entrance costs are requested.
    """
    # Base rates (LKR)
    adult_rate = 1500 if is_foreign else 300
    child_rate = 800 if is_foreign else 100
    
    vehicle_rates = {
        "car": 500,
        "van": 800,
        "bus": 1500,
        "safari_jeep": 1000
    }
    
    vehicle_fee = vehicle_rates.get(vehicle_type.lower(), 500)
    
    subtotal = (num_adults * adult_rate) + (num_children * child_rate) + vehicle_fee
    vat = subtotal * 0.18 if apply_vat else 0.0  # 18% VAT
    total = subtotal + vat
    
    return (
        f"--- Park Fee Breakdown ---\n"
        f"Adults ({num_adults} x {adult_rate}): LKR {num_adults * adult_rate}\n"
        f"Children ({num_children} x {child_rate}): LKR {num_children * child_rate}\n"
        f"Vehicle Fee ({vehicle_type}): LKR {vehicle_fee}\n"
        f"Subtotal: LKR {subtotal:.2f}\n"
        f"VAT (18%): LKR {vat:.2f}\n"
        f"---------------------------\n"
        f"Total Cost: LKR {total:.2f}"
    )
