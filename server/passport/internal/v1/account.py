from typing import Annotated

from database.controllers.account import AccountController
from fastapi import APIRouter, Depends, status
from schemas.v1 import AccountOperationOk, AccountRefund, AccountWriteOff

router = APIRouter()


@router.patch("/write_off", status_code=status.HTTP_200_OK)
async def write_off_handler(
    controller: Annotated[AccountController, Depends(AccountController)],
    write_off: AccountWriteOff,
) -> AccountOperationOk:
    return await controller.write_off_balance(write_off=write_off)


@router.patch("/refund", status_code=status.HTTP_200_OK)
async def refund_handler(
    controller: Annotated[AccountController, Depends(AccountController)],
    refund: AccountRefund,
) -> AccountOperationOk:
    return await controller.refund_balance(refund=refund)
