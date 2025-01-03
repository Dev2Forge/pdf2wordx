// Change theme (dark/light)
function changeTheme() {
  document.body.classList.toggle("dark-theme");
  darkIconTOLight();
}

function darkIconTOLight() {
  // Obtener todos los elementos con clase (.icon)
  let icon = document.querySelectorAll(".icon");
  // Definir iconos dark e iconos light para cada ícono
  // console.log(icon[1].getAttribute('name'))
  let url_icos = [];
  // Por cada ícono se agrega su nomre y sus adjetivos dark - lite
  icon.forEach((ico) => {
    let name = ico.getAttribute("name");
    let type = ico.classList[0];
    let light_icon = `https://github.com/tutosrivegamerLQ/images-projects-srm-trg/raw/main/svg-icons-flags-cursor/${type}/${name}-l.svg`;
    let dark_icon = `https://github.com/tutosrivegamerLQ/images-projects-srm-trg/raw/main/svg-icons-flags-cursor/${type}/${name}-d.svg`;
    url_icos.push([light_icon, dark_icon]);
  });

  try {
    // desde i = 0 hasta longitud de icon -1
    for (let i = 0; i < icon.length; i++) {
      // ico[i] => ico[0], ico[1]... ico[n]
      let ico = icon[i];
      //Verificar si el atributo src (img.src) es igual a iconname-dark
      if (ico.getAttribute("src") == url_icos[i][0]) {
        // Establecer ícono en light
        ico.setAttribute("src", url_icos[i][1]);
      } else {
        // Establecer ícono en dark
        ico.setAttribute("src", url_icos[i][0]);
      }
    }
  } catch (error) {
    console.error("Error: " + error);
  }
}

// Opne cualquier url sin necesidad de <a>
let urlOpen = (str) => {
  let url = new URL(str);
  open(url);
};

// Cambiar Lenguage
async function language(language, nameRadiosMain) {
  // Cambiar el idioma también del README.md
  getLanpReadme(
    nameRadiosMain,
    "pdftoword",
    "pdftoword_container",
    "btn-pdftoword-lan"
  );
  getLanpReadme(
    nameRadiosMain,
    "pdf2docx",
    "pdf2docx_container",
    "btn-pdf2docx-lan"
  );
  // Crear solicitud (para abrir el archivo con fetch)
  let solicitud = new Request(`files/language/${language}.json`);
  // Crear lista de selectores
  let selectors = [
    "#page_title",
    "#description",
    "#whats_title",
    "#spam_download",
    "#whats_pdftoword",
    "#features",
    "#how_use_title",
    "#how_use",
    "#limits",
    "#known_bugs_title",
    "#known_bugs",
    "#summary_readme_pdftoword",
    "#summary_readme_pdf2docx",
    "#comments",
  ];
  // Seleccionar la lista de contenedores
  let containers = document.querySelectorAll(selectors);

  try {
    // Solicitud de abrir y acceder al archivo
    const request = await fetch(solicitud);
    const response = await request.json();

    // Agregar el contenido correspondiente a cada elemento
    containers.forEach((element) => {
      element.innerHTML = response[element.id];
    });
  } catch (error) {
    console.error("Error en: " + error);
  }
}

function getLanMain(nameRadios) {
  let radios = document.getElementsByName(nameRadios);
  let lan;
  // Buscar entre los radios cual está seleccionado y pasar su valor a lan
  radios.forEach((radio) => {
    if (radio.checked) {
      lan = radio.value;
      if (radio.checked) {
        checkSelectedLan(lan);
        btnFlagLan("btn-main-lan", radio.value);
      }
    }
  });
  language(lan, nameRadios);
}

// Poner en checked los readme al mismo idioma del principal
function checkSelectedLan(lan) {
  let docx2 = document.getElementsByName("lan-pdf2docx");
  let docxto = document.getElementsByName("lan-pdftoword");
  docx2.forEach((language) => {
    if (language.value == lan) {
      language.checked = true;
    } else {
      language.checked = false;
    }
  });
  docxto.forEach((language) => {
    if (language.value == lan) {
      language.checked = true;
    } else {
      language.checked = false;
    }
  });
}

// Obtener contenido de un README.md y ponerlo en el HTML
async function fetchReadmeMD(file, idHtmlObject) {
  // Agregar el contenido de readme_pdf2docx al blockquote
  const readme_pdf2docx = new Request(file);
  let containerBlockQuote = document.querySelector(`#${idHtmlObject}`);

  try {
    const request = await fetch(readme_pdf2docx);
    const response = await request.text();

    let htmlContent = marked.marked(response);
    containerBlockQuote.innerHTML = htmlContent;
  } catch (error) {
    console.error("Error: " + error);
  }
}

function getLanpReadme(nameRadios, nameFile, idContainer, idImgLan) {
  // let select = document.querySelector(`#${idSelect}`);
  let lans = document.getElementsByName(nameRadios);
  let lan;
  // El lenguaje será el radio seleccionado
  lans.forEach((lanRadio) => {
    if (lanRadio.checked) {
      lan = lanRadio.value;
      if (lanRadio.checked) {
        btnFlagLan(idImgLan, lanRadio.value);
      }
    }
  });
  const pdftowordLanguaje = `files/blockquote/readme_${nameFile}_${lan}.md`;
  fetchReadmeMD(pdftowordLanguaje, idContainer);
}

// Ejecutar cambio de lenguajes cuando se haga un cambio
function lanOnChangeMain() {
  let radios = document.getElementsByName("lan-main");
  radios.forEach((radio) => {
    radio.setAttribute("onchange", 'radiosLanWho("lan-main")');
  });
}
function lanOnChangePdfToWord() {
  let radios = document.getElementsByName("lan-pdftoword");
  radios.forEach((radio) => {
    radio.setAttribute("onchange", 'radiosLanWho("lan-pdftoword")');
  });
}
function lanOnChangePdf2Docx() {
  let radios = document.getElementsByName("lan-pdf2docx");
  radios.forEach((radio) => {
    radio.setAttribute("onchange", 'radiosLanWho("lan-pdf2docx")');
  });
}

function radiosLanWho(nameRadios) {
  switch (nameRadios) {
    case "lan-main":
      getLanMain("lan-main");
      break;
    case "lan-pdftoword":
      getLanpReadme(
        "lan-pdftoword",
        "pdftoword",
        "pdftoword_container",
        "btn-pdftoword-lan"
      );
      break;
    case "lan-pdf2docx":
      getLanpReadme(
        "lan-pdf2docx",
        "pdf2docx",
        "pdf2docx_container",
        "btn-pdf2docx-lan"
      );
      break;
  }
}

// Cambiar la imagen del botón de lenguaje según idioma seleccionado
function btnFlagLan(id, lan) {
  let imgButton = document.querySelector(`#${id}`);
  imgButton.setAttribute(
    "src",
    `https://github.com/tutosrivegamerLQ/images-projects-srm-trg/raw/main/svg-icons-flags-cursor/flags-svg/flag-${lan}.svg`
  );
}

// Popover
function pop() {
  const html =
    '<button id="btn-tog" popovertarget="banner-ouo" popovertargetaction="toggle"></button>';
  document.body.insertAdjacentHTML("afterend", html);
  const btn = document.querySelector("#btn-tog");
  btn.click();
  btn.remove();
}

function main() {
  // Ejecutar la selección del lenguaje
  getLanMain("lan-main");
  // Poner tema oscuro por defecto
  changeTheme();
  // Lenguaje por defecto del README.md
  // getLanpdf2docx('selectLanpdf2docx');
  getLanpReadme(
    "lan-pdftoword",
    "pdftoword",
    "pdftoword_container",
    "btn-pdftoword-lan"
  );
  getLanpReadme(
    "lan-pdf2docx",
    "pdf2docx",
    "pdf2docx_container",
    "btn-pdf2docx-lan"
  );

  // Asignar función cuando cambia lenguaje
  lanOnChangeMain("lan-main");
  lanOnChangePdfToWord("lan-pdftoword");
  lanOnChangePdf2Docx("lan-pdf2docx");
  pop();
}
