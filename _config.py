config={"name":"pool","host":"127.0.0.1","user":"fish", "password":"5tgb6yhn", "database":"test", "size":4}

sqlstrings = {
    # simple
    "member"    : {
        "sql"   : "SELECT member_id, nick_name from member limit %(offset)s , %(limit)s", 
        "params": {"offset":0,"limit":100}, 
    },
    # with parameters
    "payment"   : {
        "sql"   : 'SELECT * FROM payment WHERE (payment_id= %(payment_id)s or %(payment_id)s = -99999) limit %(offset)s , %(limit)s',
        "params": {"payment_id": -99999 ,"offset":0,"limit":100},
    },
}

html={
    "root": '''
    <head><meta http-equiv="Content-Type" content="text/html; charset=utf-8"></head>
    <h2>ぷん！おやすみずき</h2>
    <iframe width="580" height="315"
      src="https://www.youtube.com/embed/videoseries?list=PLYyzGNAghtgN50T0C-5iVXsevu1sHSKSz"
      frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope;picture-in-picture" allowfullscreen="">
    </iframe>
''',

}


package_title='''
 __    _  ___   __   __  _______  ______      ______    _______  _______  _______  _______  __   __  ___     
|  |  | ||   | |  | |  ||       ||    _ |    |    _ |  |       ||       ||       ||       ||  | |  ||   |    
|   |_| ||   | |  | |  ||    ___||   | ||    |   | ||  |    ___||  _____||_     _||    ___||  | |  ||   |    
|       ||   | |  |_|  ||   |___ |   |_||_   |   |_||_ |   |___ | |_____   |   |  |   |___ |  |_|  ||   |    
|  _    ||   | |       ||    ___||    __  |  |    __  ||    ___||_____  |  |   |  |    ___||       ||   |___ 
| | |   ||   | |       ||   |___ |   |  | |  |   |  | ||   |___  _____| |  |   |  |   |    |       ||       |
|_|  |__||___| |_______||_______||___|  |_|  |___|  |_||_______||_______|  |___|  |___|    |_______||_______|
'''
