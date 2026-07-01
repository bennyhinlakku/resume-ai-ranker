SERVICE_COMPANIES = {
    "infosys",
    "tcs",
    "wipro",
    "accenture",
    "cognizant",
    "capgemini",
    "mindtree",
    "tech mahindra",
    "hcl"
}


def analyze_company_history(companies):

    service = 0
    product = 0

    for company in companies:

        if company.lower() in SERVICE_COMPANIES:
            service += 1
        else:
            product += 1

    return {
        "service_experience": service,
        "product_experience": product,
        "consulting_only": (
            service > 0 and product == 0
        )
    }


if __name__ == "__main__":

    sample = [
        "Mindtree",
        "Dunder Mifflin"
    ]

    print(analyze_company_history(sample))
    