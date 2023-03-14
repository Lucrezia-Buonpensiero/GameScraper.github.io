$.fn.ajax_searching = function () {
    let show_elem = 'show'
    let results = $('#results');
    let loader = $('#loader');
    let field_text = $('#search_concept').text();
    let query_text = $('#search').val();

    results.removeClass(show_elem)
    loader.addClass(show_elem);

    $.ajax({
        url: 'get_results',
        method: 'POST',
        data: jQuery.param({ field: field_text, query: query_text }) ,
        contentType: 'application/x-www-form-urlencoded; charset=UTF-8',
        success: function(data) {

            $('#results_list').html(data);
            results.addClass(show_elem)
            loader.removeClass(show_elem);

        },
        error: function(data) {
            console.log(data);
        }
    });
};

$(document).ready(function(e) {

    $('#button-search').click(function(e){
        $.fn.ajax_searching();
    });

    $('#search').keyup(function(e){
        if(e.keyCode === 13)
            $.fn.ajax_searching();
    });

    $('.search-panel .dropdown-menu').find('a').click(function(e) {
        e.preventDefault();
        let param = $(this).attr('href').replace('#','');
        let concept = $(this).text();
        $('.search-panel span#search_concept').text(concept);
        $('.input-group #search_param').val(param);
    });

});
