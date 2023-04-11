// Search select
const baseUrl = "http://127.0.0.1:5000/"

var url = baseUrl


// select by genre
function genreSelected(selectedGenre)
{
    url = baseUrl+"getByGenre";
    $.post(url, {
        genre: selectedGenre,
    },function(data, status) {
        console.log(data, status);
        var htmlContent = "<h2 id='heading'>" + selectedGenre + "</h2><div class='row'>";
        for(var i=0; i<data[0].genre_movies.length; i++) {
            htmlContent = htmlContent + "<div class='col-6 col-sm-4 col-md-2 movie-card'><a href='/movie/"+data[0].genre_movies[i]+"'><img src='"+data[1].genre_posters[i]+"' alt='' style='width: 100%;height: auto;'><p>"+data[0].genre_movies[i]+"</p></a></div>";
        }
        htmlContent += "</div>";
        document.getElementById("genre-row").innerHTML = htmlContent;
    });
}

function yearSelected(selectedYear)
{
    url = baseUrl+"getByYear";
    $.post(url, {
        year: selectedYear,
    },function(data, status) {
        console.log(data, status);
        var htmlContent = "<h2 id='heading'>" + selectedYear + "</h2><div class='row'>";
        for(var i=0; i<data[0].year_movies.length; i++) {
            htmlContent = htmlContent + "<div class='col-6 col-sm-4 col-md-2 movie-card'><a href='/movie/"+data[0].year_movies[i]+"'><img src='"+data[1].year_posters[i]+"' alt='' style='width: 100%;height: auto;'><p>"+data[0].year_movies[i]+"</p></a></div>";
        }
        htmlContent += "</div>";
        document.getElementById("year-row").innerHTML = htmlContent;
    });
}

$(document).ready(function(){
    $('#search').keyup(function(){
        var search = $(this).val();
        if(search != ''){
            $.ajax({
                url: '/autocomplete?search=' + search,
                success: function(response){
                    if(response.length > 0){
                        var autocompleteList = '<div class="autocomplete-items">';
                        for(var i = 0; i < response.length; i++){
                            autocompleteList += '<div>' + response[i][0] + '</div>';
                        }
                        autocompleteList += '</div>';
                        $('#autocomplete-container').html(autocompleteList);
                    } else {
                        $('#autocomplete-container').html('');
                    }
                }
            });
        } else {
            $('#autocomplete-container').html('');
        }
    });
    $('body').on('click', '.autocomplete-items div', function(){
        $('#search').val($(this).text());
        $('#autocomplete-container').html('');
    });

    $(document).click(function(event) {
        if (!$(event.target).closest('.autocomplete-items').length) {
            $('#autocomplete-container').html('');
        }
    });
});

function movieSelected()
{
    let selectedmovie = document.getElementById("search").value;
    url = baseUrl+"movie/"+selectedmovie;
    window.location.href=url;
    document.getElementById('search').value="";
}
