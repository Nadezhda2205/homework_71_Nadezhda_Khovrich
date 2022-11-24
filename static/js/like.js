
$(document).ready(function() {

    $('.like').on('click', function(e) {
        e.preventDefault();
        let pk_post = e.target.id;

        url = `http://127.0.0.1:8000/api/posts/${ pk_post }/like/`

    fetch(url)
    .then((response) => {

        img = document.getElementById(pk_post)
        img.setAttribute('src', '/static/icon/heart_like.png');
        $(this).removeClass('like').addClass('unlike')
        return response;
        })
    });

    $('.unlike').on('click', function(e) {
        e.preventDefault();
        let pk_post = e.target.id;
        url = `http://127.0.0.1:8000/api/posts/${ pk_post }/unlike/`

    fetch(url)
    .then((response) => {

        img = document.getElementById(pk_post)
        img.setAttribute('src', '/static/icon/heart_unlike.png');
        $(this).removeClass('unlike').addClass('like')

        return response;
        })
   

    })

    })


