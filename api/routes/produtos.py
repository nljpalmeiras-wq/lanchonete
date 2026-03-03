from fastapi import APIRouter, HTTPException
from schemas.produto import ProdutoCreate, ProdutoOut, ProdutoAlterarValor
from services.lanchonete_service import service

router = APIRouter(prefix="/produtos", tags=["produtos"])

@router.post("", response_model=ProdutoOut)
def criar(payload: ProdutoCreate):
    produto = service.criar_produto(
        payload.codigo,
        payload.valor,
        payload.tipo,
        payload.desconto_percentual
    )
    return ProdutoOut(**produto.__dict__)