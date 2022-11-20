
from OrekiRobot import DRAGONS
from OrekiRobot.modules.helper_funcs.telethn import IMMUNE_USERS, tbot


async def user_is_ban_protected(user_id: int, message):
    status = False
    if message.is_private or user_id in (IMMUNE_USERS):
        return True

    async for user in tbot.iter_participants(
        message.chat_id,
        filter=ChannelParticipantsAdmins,
    ):
        if user_id == user.id:
            status = True
            break
    return status


async def user_is_admin(user_id: int, message):
    status = False
    if message.is_private:
        return True

    async for user in tbot.iter_participants(
        message.chat_id,
        filter=ChannelParticipantsAdmins,
    ):
        if user_id == user.id or user_id in DRAGONS:
            status = True
            break
    return status


async def user_is_admin(user_id: int, message):
    status = False
    if message.is_private:
        return True

    async for user in tbot.iter_participants(
        message.chat_id,
        filter=ChannelParticipantsAdmins,
    ):
        if user_id == user.id or user_id in DRAGONS:
            status = True
            break
    return status


async def user_is_admin(user_id: int, message):
    status = False
    if message.is_private:
        return True

    async for user in tbot.iter_participants(
        message.chat_id,
        filter=ChannelParticipantsAdmins,
    ):
        if user_id == user.id or user_id in DRAGONS:
            status = True
            break
    return status


async def is_user_admin(user_id: int, chat_id):
    status = False
    async for user in tbot.iter_participants(
        chat_id,
        filter=ChannelParticipantsAdmins,
    ):
        if user_id == user.id or user_id in DRAGONS:
            status = True
            break
    return status


async def cutiepii_is_admin(chat_id: int):
    status = False
    cutiepii = await tbot.get_me()
    async for user in tbot.iter_participants(
        chat_id,
        filter=ChannelParticipantsAdmins,
    ):
        if cutiepii.id == user.id:
            status = True
            break
    return status


async def is_user_in_chat(chat_id: int, user_id: int):
    status = False
    async for user in tbot.iter_participants(chat_id):
        if user_id == user.id:
            status = True
            break
    return status


async def can_change_info(message):
    return message.chat.admin_rights.change_info if message.chat.admin_rights else False


async def can_ban_users(message):
    return message.chat.admin_rights.ban_users if message.chat.admin_rights else False


async def can_pin_messages(message):
    return (
        message.chat.admin_rights.pin_messages if message.chat.admin_rights else False
    )


async def can_invite_users(message):
    return (
        message.chat.admin_rights.invite_users if message.chat.admin_rights else False
    )


async def can_add_admins(message):
    return message.chat.admin_rights.add_admins if message.chat.admin_rights else False


async def can_delete_messages(message):

    if message.is_private:
        return True
    if message.chat.admin_rights:
        return message.chat.admin_rights.delete_messages
    return False
