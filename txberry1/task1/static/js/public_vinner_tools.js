/** public_vinner_tools.js
 *
 */


/** pytanie o zwycięzców dla team-id
 *
 */
function ask_pizza_vinners() {

    var toSend = new Object();
    toSend.name = 'pizza-topping-podium';
    toSend.dt = null;
    send_xhttp_post_request_csrf(rest_url, toSend, calbaack_teamid_vinners);
    setTimeout(function(){
        ask_pizza_vinners();
    }, 5 * 1000);
}

/** tutaj wchodzi gdy odbierze zwycięzców
 *
 */
function calbaack_teamid_vinners(resp_obj) {

    //console.log(resp_obj);
    var pprefix = 'p';
    // lista ID obecnych w templatce
    var set_list = [pprefix + "place_1", pprefix + "place_2", pprefix + "place_3"];
    for(var i=0;i<set_list.length;i++) {
        var place_x = document.getElementById(set_list[i]);
        card_data_replace_for_moment(pprefix, place_x, resp_obj.pizza_list, i);
    }

    // sprawdź, czy to coś nowego i jeśli tak dodaj wiersz i przerysuj wykres
    //chartMidAddRowRedraw( resp_obj.data_mid );
    // zaktualizuj też Donuta z podziałem na ilość głosów
    //chartDonutCountUpdateRedraw( resp_obj.data_count );
}

ask_pizza_vinners();
