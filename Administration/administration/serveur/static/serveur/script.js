function toggleDropdown(btn) {
    // Ferme tous les autres menus
    document.querySelectorAll('.dropdown-menu').forEach(menu => {
        if (menu !== btn.nextElementSibling) menu.classList.remove('show');
    });
    // Ouvre/ferme celui cliqué
    btn.nextElementSibling.classList.toggle('show');
}
// Ferme le menu si on clique ailleurs
document.addEventListener('click', function(e) {
    if (!e.target.closest('.action-btn')) {
        document.querySelectorAll('.dropdown-menu').forEach(menu => menu.classList.remove('show'));
    }
});