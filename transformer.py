def transform_rest(users):
    return [{"name": u["name"], "email": u["email"], "source": "REST"} for u in users]

def transform_graphql(countries):
    return [{"name": c["name"], "email": f"{c['code'].lower()}@country.com", "source": "GraphQL"} for c in countries]
