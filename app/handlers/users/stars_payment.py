import logging
import aiohttp

from aiogram import Router, F
from aiogram.types import Message

from app.core.config import settings

router = Router()


@router.pre_checkout_query()
async def pre_checkout_query_handler(pre_checkout_query):
    """
    Handle pre-checkout query for Telegram Stars payment
    """
    await pre_checkout_query.answer(ok=True)


@router.message(F.successful_payment)
async def successful_payment_handler(message: Message):
    """
    Handle successful Telegram Stars payment and notify backend webhook
    """
    payment = message.successful_payment
    
    transaction_id = int(payment.invoice_payload)
    transaction_hash = payment.telegram_payment_charge_id
    amount = payment.total_amount
    
    logging.info(
        f"Payment received: transaction_id={transaction_id}, "
        f"amount={amount}, hash={transaction_hash}"
    )
    
    webhook_url = f"{settings.BACKEND_URL}/webhook/stars"
    payload = {
        "transaction_id": transaction_id,
        "transaction_hash": transaction_hash,
        "amount": amount,
        "secret_key": settings.SECRET_KEY.get_secret_value()
    }
    
    headers = {
        "Content-Type": "application/json"
    }
    

    try:
        async with aiohttp.ClientSession() as session:
            logging.info(f"Sending POST to {webhook_url} with payload: {payload}")
            async with session.post(
                webhook_url, 
                json=payload, 
                headers=headers,
                allow_redirects=False
            ) as response:
                response_text = await response.text()
                logging.info(f"Webhook response: status={response.status}, body={response_text}")
                
                if response.status == 200:
                    logging.info(f"Webhook sent successfully for transaction {transaction_id}")
                    await message.answer(
                        "✅ Payment successful! Your account has been credited."
                    )
                else:
                    logging.error(
                        f"Webhook failed for transaction {transaction_id}: "
                        f"status={response.status}, error={response_text}"
                    )
                    await message.answer(
                        "⚠️ Payment received but there was an issue processing it. "
                        "Please contact support if your balance is not updated."
                    )
    except Exception as e:
        logging.error(f"Error sending webhook for transaction {transaction_id}: {e}", exc_info=True)
        await message.answer(
            "⚠️ Payment received but there was an issue processing it. "
            "Please contact support if your balance is not updated."
        )
