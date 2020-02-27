/** podium_tools.js
 *
 */

/** jeśli nastąpiła zmiana na pozycji podjalnej,
 *  odwróć kartę, podmień i po chwili odwróć znów,
 *  gdy brak do podmiany - pozostaw odwróconą/niewidoczną
 */
function card_data_replace_for_moment(pprefix, place_x, resp_obj_vinners, i) {

    var card = place_x.children[0].children[0].children[0];
    var bold_label = '';
    var img_url = '';
    var item_id = '';
    if(resp_obj_vinners && i < resp_obj_vinners.length && resp_obj_vinners[i]) {
        bold_label = resp_obj_vinners[i][1];
        img_url = resp_obj_vinners[i][2];
        item_id = resp_obj_vinners[i][0];
    }
    if ( card.children[2].id != pprefix + "item_" + item_id ) {
        place_x.style.transform = "rotateY(90deg)";  // OK! dobrze się zachowa gdy nie będzie a potem się pojawi
        setTimeout(function(){
            card_data_replace(pprefix,
                              place_x,
                              item_id,
                              bold_label,
                              img_url);
            if(item_id != '') {
                // ponownie uczyć widoczną / odwróć znów - tylko gdy jest jakiś
                place_x.style.transform = "rotateY(0deg)";
            }
        }, 1200); // czas po jakim podmienia (czyli podmienia gdy jest odwrócona/niewidoczna)
    }
}

/** podmień dane w karcie, obrazek i opisy oraz ID
 *
 */
function card_data_replace(pprefix, place_x, item_id, bold_label, team_player_img_url) {

    var card = place_x.children[0].children[0].children[0];
    card.children[0].src = "/static/dagrasso_pliki/" + team_player_img_url;
    card.children[0].alt = bold_label;
    card.children[1].children[0].innerHTML = bold_label;
    card.children[2].id = pprefix + 'item_' + item_id;
}
