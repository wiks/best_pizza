/** voting.js
 *
 */

/** pizza voting
 *
 */
function clickedPizzaId(pizza_id) {

    var toSend = new Object();
    toSend.name = 'pizza_vote';
    toSend.pizza_id = pizza_id;
    console.info(toSend);
    send_xhttp_post_request_csrf(rest_url,
                                 toSend,
                                 work_with_rest_respond);
}

/** response for voting
 *
 */
function work_with_rest_respond(resp_obj) {

    document.getElementById("xberryModalLabel").innerHTML = resp_obj.name + ' głosów: ' + resp_obj.votes;
    var ih = '';
    if(resp_obj.most_liked_topping) {
        ih += 'najbardziej ulubione dodatki: <br>';
        for(var i = 0; i < resp_obj.most_liked_topping.length; i++) {
            if(i > 0) {
                ih += ',';
            };
            ih += '' + resp_obj.most_liked_topping[i];
        }
    }
    document.getElementById("modal-body").innerHTML = ih;
    $('#xberryModal').modal('show');
}
