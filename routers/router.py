import strings

from aiogram import Router
from aiogram import filters
from aiogram import types

router = Router()

@router.message(filters.CommandStart())
async def start(message: types.Message, command: filters.CommandObject):
    print(command.args)
    
    buttons = [
        [
            types.KeyboardButton(text=strings.KEYBOARD.PROFILE),
            types.KeyboardButton(text=strings.KEYBOARD.BUY)
        ],
        [
            types.KeyboardButton(text=strings.KEYBOARD.HELP),
            types.KeyboardButton(text=strings.KEYBOARD.REFERRAL)
        ]
    ]

    row_for_subscribers = 1
    if True:  # TODO: check subscription
        buttons.insert(
            row_for_subscribers,
            [
                types.KeyboardButton(text=strings.KEYBOARD.APP), types.KeyboardButton(
                    text=strings.KEYBOARD.CONFIG)
            ],
        )
    await message.answer(
        strings.GREETING,
        reply_markup=types.ReplyKeyboardMarkup(
            keyboard=buttons,
            resize_keyboard=True,
        )
    )

@router.message()
async def message(message: types.Message):
    match message.text:
        case strings.KEYBOARD.PROFILE:
            await message.answer(strings.PROFILE(message.from_user.full_name, "TODO: подписка", "TODO: дата"))
        case strings.KEYBOARD.BUY:
            await message.answer("Тут должно быть получение...")
        case strings.KEYBOARD.APP:
            await message.answer(
                strings.APP.MESSAGE,
                reply_markup=types.InlineKeyboardMarkup(
                    inline_keyboard=[
                        [
                            types.InlineKeyboardButton(
                                text=strings.APP.BUTTONS.ANDROID, callback_data=strings.APP.CALLBACK.ANDROID),
                            types.InlineKeyboardButton(
                                text=strings.APP.BUTTONS.IOS, callback_data=strings.APP.CALLBACK.IOS)
                        ],
                        [
                            types.InlineKeyboardButton(
                                text=strings.APP.BUTTONS.WINDOWS, callback_data=strings.APP.CALLBACK.WINDOWS),
                            types.InlineKeyboardButton(
                                text=strings.APP.BUTTONS.MACOS, callback_data=strings.APP.CALLBACK.MACOS)
                        ],
                        [types.InlineKeyboardButton(
                            text=strings.APP.BUTTONS.OTHER,
                            callback_data=strings.APP.CALLBACK.OTHER
                        )]
                    ]
                )
            )
        case strings.KEYBOARD.CONFIG:
            await message.answer("Тут должен спавница конфиг...")
        case strings.KEYBOARD.HELP:
            await message.answer(strings.HELP)
        case strings.KEYBOARD.REFERRAL:
            await message.answer(strings.REFERRAL(message.from_user.id))


@router.callback_query()
async def callback(query: types.CallbackQuery):
    await query.answer()
    if query.data in strings.APP.CALLBACK.__dict__.values():
        await query.message.answer(
            getattr(strings.APP.ANSWER, query.data.upper()),
            reply_markup=types.InlineKeyboardMarkup(
                inline_keyboard=[[types.InlineKeyboardButton(
                    text=strings.APP.OPEN, 
                    url=getattr(strings.APP.LINKS, query.data.upper())
                )]]
            ), parse_mode="Markdown"
        )