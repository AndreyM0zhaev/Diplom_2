class ResponseText:

    ORDER                   = 'order'
    ORDERS                  = 'orders'
    TOTAL                   = 'total'
    TOTAL_TODAY             = 'totalToday'
    SUCCESS                 = 'success'
    MESSAGE                 = 'message'
    CREATE_DOUBLE_USER      = 'User already exists'
    SERVER_ERROR            = 'Internal Server Error'
    UNAUTHORIZED            = 'You should be authorised'
    MISSING_REQUIRED_FIELD  = 'Email, password and name are required fields'


class StatusCode:

    OK                      = 200
    CREATED                 = 201
    ACCEPTED                = 202
    BAD_REQUEST             = 400
    UNAUTHORIZED            = 401
    FORBIDDEN               = 403
    NOT_FOUND               = 404
    INTERNAL_SERVER_ERROR   = 500
