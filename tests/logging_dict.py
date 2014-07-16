logging_dict = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': ('%(asctime)s. - %(name)s - %(levelname)s - '
                       '%(message)s')
        },
        'verbose': {
            'format': ('%(asctime)s - %(name)s - %(levelname)s - ',
                       '%(module)s %(funcName)s %(pathname)s ',
                       '%(lineno)s - %(message)s')
        }
    },
    'handlers': {
        'console': {
            'formatter': 'simple',
            'class': 'logging.StreamHandler',
            'level':
            'DEBUG'
        }
    },
    'root': {
        'handlers': ['console'],
        'level': 'DEBUG'
    }
}
