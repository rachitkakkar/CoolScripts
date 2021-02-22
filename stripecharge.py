import stripe
stripe.api_key = "token

client = stripe.Token.create(
  card={
    'number': 4242424242424242,
    'exp_month': 2,
    'exp_year': 2021,
    'cvc': 123,
    },
)

charge = stripe.Charge.create(
  amount=100,
  currency="usd",
  source=client['id'],
  description="Test charge"
)
