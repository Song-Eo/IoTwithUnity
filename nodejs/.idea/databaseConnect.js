const mysql = require('mysql');

module.exports = function (){
    return {
        init: function () {
         return mysql.createConnection({
            host: 'localhost',
            port: 3036,
            user: 'rooti',
            password: 'Threego!!',
            database: 'threego'
         })
        },

        db_open: function (con) {
            con.connect()
        }
    }
}