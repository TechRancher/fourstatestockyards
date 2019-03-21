/**
 * Toggle footer_nav
 * 
 */

var nav = document.getElementById('access_nav'),
    footer = document.getElementById('footer');

nav.addEventListener('click', function(e){
    footer.className = footer.className? '': 'with_nav';
    e.preventDefault();
});