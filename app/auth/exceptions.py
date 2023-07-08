from app.exceptions import BadRequestException, NotAuthenticatedException


class EmailTakenException(BadRequestException):
    DETAIL = 'User with this email already exists'


class InvalidCredentialsException(NotAuthenticatedException):
    DETAIL = 'Invalid data entered'


class TokenAbsentException(NotAuthenticatedException):
    DETAIL = 'Token missing'
