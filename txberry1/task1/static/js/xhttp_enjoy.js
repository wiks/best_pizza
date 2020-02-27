

/** proobuje
 * to zuniwersalnic
 */
function send_xhttp_post_request_csrf(url, toSend, calbaack_function=null) {

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            try {
                resp_obj = JSON.parse(this.responseText);
                if(calbaack_function){
                    calbaack_function(resp_obj);
                }
            }
            catch(err) {
                console.info('response error');
            }
        }
    };
    xhttp.open("POST", url, true);
    var csrftoken = getCookie('csrftoken');
    xhttp.setRequestHeader("X-CSRFToken", csrftoken);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send(JSON.stringify(toSend));
}


/** proobuje
 * to zuniwersalnic
 */
function send_xhttp_post_request_no_csrf(url, toSend, calbaack_function=null) {

    var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState == 4 && this.status == 200) {
                //alert(this.responseText);
                resp_obj = JSON.parse(this.responseText);
                if(calbaack_function){
                    calbaack_function(resp_obj);
                }
        }
    };
    xhttp.open("POST", url, true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send(JSON.stringify(toSend));
}


