const headerUserMenuButton = document.getElementById("user-menu-button");

const menu = document.getElementById("header-menu")

headerUserMenuButton.onclick = () => {
    menu.style.display = menu.style.display === 'none' ? 'initial' : 'none'
}