const form = document.querySelector('form');
const titleInput = document.querySelector('#title');
const authorInput = document.querySelector('#author')
const descInput = document.querySelector('#description');
const statusInput = document.querySelector('#status');
const bookList = document.querySelector('#book-list');

let myLibrary = [];

function Book(title, author, description, status) {
  this.title = title;
  this.author = author;
  this.descripion = description;
  this.status = status;
}

function addBookToLibrary() {
  const newBook = new Book(titleInput.value, authorInput.value,
    descInput.value, statusInput.value);
  myLibrary.push(newBook);
  localStorage.setItem('myLibrary', JSON.stringify(myLibrary));
}

function displayBooks() {
  bookList.innerHTML = '';
  myLibrary.forEach((book, index) => {
    const bookDiv = document.createElement('div');
    bookDiv.classList.add('book');

    const title = document.createElement('h3');
    title.textContent = book.title;

    const author = document.createElement('p');
    author.textContent = `By ${book.author}`;

    const description = document.createElement('p');
    description.textContent = book.descripion;
    description.classList.add('description');

    const status = document.createElement('p');
    status.classList.add('status');

    switch (book.status) {
      case 'read':
        status.textContent = 'read';
        status.style.color = 'green';
        break;
      case 'to-read':
        status.textContent = 'to read';
        status.style.color = 'red';
        break;
      case 'reading':
        status.textContent = 'reading';
        status.style.color = 'orange';
        break;
      default:
        break;
    }

    const deleteBtn = document.createElement('button');
    deleteBtn.classList.add('delete-btn');
    deleteBtn.textContent = 'Delete';
    deleteBtn.addEventListener('click', () => {
      myLibrary.splice(index, 1);
      localStorage.setItem('myLibrary', JSON.stringify(myLibrary));
      displayBooks();
    });

    const editBtn = document.createElement('button');
    editBtn.classList.add('edit-btn');
    editBtn.textContent = 'Edit';
    editBtn.addEventListener('click', () => {
      titleInput.value = book.title;
      authorInput.value = book.author;
      descInput.value = book.descripion;
      statusInput.value = book.status;

      // Remove the current book from the library
      myLibrary.splice(index, 1);
      localStorage.setItem('myLibrary', JSON.stringify(myLibrary));
      displayBooks();
    });

    bookDiv.append(title, author, description, status, editBtn, deleteBtn);
    bookList.appendChild(bookDiv);
  });
}

form.addEventListener('submit', (e) => {
  e.preventDefault();
  addBookToLibrary();
  form.reset();
  displayBooks();
});

if (localStorage.getItem('myLibrary')) {
  myLibrary = JSON.parse(localStorage.getItem('myLibrary'));
  displayBooks();
}