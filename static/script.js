// Функція для динамічного додавання поля введення та кнопки
function increaseHeight() {
    var taskContainer = document.querySelector('.task_container');

    // Створюємо новий контейнер для поля введення та кнопки
    var newInputContainer = document.createElement('div');
    newInputContainer.classList.add('input-container');
    newInputContainer.style.display = "flex"; // Розташування елементів в рядок
    newInputContainer.style.alignItems = "center"; // Вирівнювання по центру
    newInputContainer.style.margin = "10px 0"; // Відступи між елементами

    // Створюємо поле для введення
    var newInput = document.createElement('input');
    newInput.classList.add('goal_input');
    newInput.type = "text";
    newInput.placeholder = "Enter your goal here...";
    newInput.style.marginRight = "10px"; // Відступ між полем і кнопкою

    // Створюємо кнопку
    var newButton = document.createElement('button');
    newButton.classList.add('goal_button');
    newButton.textContent = "Add";

    // Додаємо подію на кнопку для відправки форми
    newButton.addEventListener('click', function(event) {
        event.preventDefault();  // запобігає перезавантаженню сторінки
        var goalText = newInput.value;
        if (goalText) {
            // Надсилаємо дані через fetch
            fetch('/add_task', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: 'title=' + encodeURIComponent(goalText)
            })
            .then(response => response.json()) // обробляємо JSON відповідь
            .then(data => {
                alert(data.message); // виведемо успішне повідомлення
                // Додаємо нову задачу на сторінку
                addTaskToPage(goalText);
            })
            .catch(error => {
                console.error('Error:', error);
            });
        }
    });

    // Додаємо поле введення та кнопку до контейнера
    newInputContainer.appendChild(newInput);
    newInputContainer.appendChild(newButton);

    // Додаємо контейнер до основного контейнера
    taskContainer.appendChild(newInputContainer);

    // Переміщуємо кнопку (при необхідності) під новим елементом
    var addButton = document.querySelector('.add_deadline_button');
    taskContainer.appendChild(addButton); // Переміщаємо кнопку в кінець контейнера
}

// Функція для додавання задачі на сторінку
function addTaskToPage(taskTitle) {
    var taskContainer = document.querySelector('.task_container');

    var newTask = document.createElement('div');
    newTask.classList.add('task');
    newTask.textContent = taskTitle;
    
    taskContainer.appendChild(newTask);
}
