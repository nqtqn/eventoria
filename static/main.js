function openModal() {
  document.getElementById('cityModal').style.display = 'flex';
}

function closeModal() {
  document.getElementById('cityModal').style.display = 'none';
}

function closeModalOutside(event) {
  var modal = document.getElementById('cityModal');
  if (event.target === modal) {
    closeModal();
  }
}

function filterCities() {
  // Get input value and convert to lowercase for case-insensitive search
  var input = document.getElementById('citySearch').value.toLowerCase();
  
  // Get the list of cities
  var cities = document.getElementById('cityList').getElementsByTagName('li');

  // Loop through the cities and hide those that don't match the search input
  for (var i = 0; i < cities.length; i++) {
    var cityName = cities[i].textContent || cities[i].innerText;

    if (cityName.toLowerCase().indexOf(input) > -1) {
      cities[i].style.display = '';
    } else {
      cities[i].style.display = 'none';
    }
  }
}





function filterCities() {
  // Get input value and convert to lowercase for case-insensitive search
  var input = document.getElementById('citySearch').value.toLowerCase();

  // Get the list of cities and modal content
  var cityList = document.getElementById('cityList');
  var modalContent = document.querySelector('.modal-content');

  // Loop through the cities and hide those that don't match the search input
  for (var i = 0; i < cityList.children.length; i++) {
    var cityName = cityList.children[i].textContent || cityList.children[i].innerText;

    if (cityName.toLowerCase().indexOf(input) > -1) {
      cityList.children[i].style.display = '';
    } else {
      cityList.children[i].style.display = 'none';
    }
  }

  // Check if the city list height exceeds the modal content height
  if (cityList.offsetHeight > modalContent.clientHeight) {
    // Hide the scrollbar for the modal content
    modalContent.style.overflowY = 'hidden';
  } else {
    // Show the scrollbar if needed
    modalContent.style.overflowY = 'auto';
  }
}



document.addEventListener('DOMContentLoaded', function () {
  const burgerIcon = document.getElementById('burger-icon');
  const menu = document.getElementById('menu');

  burgerIcon.addEventListener('click', function () {
    if (menu.style.display === 'block') {
      menu.classList.add('menu-closed');
      setTimeout(() => {
        menu.style.display = 'none';
        menu.classList.remove('menu-closed');
      }, 300);
    } else {
      menu.style.display = 'block';
    }
  });
});