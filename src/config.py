class DevelopmentConfig():
    DEBUG=True
    MYSQL_HOST='localhost'
    MYSQL_USER='Marsillo'
    MYSQL_PASSWORD='Rabito'
    MYSQL_DB='api_utl'
    MYSQL_CURSORCLASS ='Cursor'
    
config={
    'development':DevelopmentConfig
}