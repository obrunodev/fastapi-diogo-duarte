from fastapi import APIRouter

router = APIRouter()

# Path parameter -> Faz parte do caminho

# Query parameter -> Segue depois da interrogação
# Ex.: https://example.com/from_currency=BRL/?to_currencies=USD,EUR&price=15

# Body parameter -> Não usado nesse projeto


@router.get('/converter/{from_currency}')
def converter(from_currency: str, to_currencies: str, price: float):
    return {'message': 'Valor convertido'}
