// Change theme (dark/light)
function changeTheme() {
  document.body.classList.toggle("dark-theme");
  darkIconTOLight();
}

function darkIconTOLight() {
  // Obtener todos los elementos con clase (.icon)
  var icon = document.querySelectorAll(".icon");
  // Definir iconos dark e iconos light para cada ícono
  // console.log(icon[1].getAttribute('name'))
  var url_icos = [];
  // Por cada ícono se agrega su nomre y sus adjetivos dark - lite
  icon.forEach((ico) => {
    var name = ico.getAttribute("name");
    var type = ico.classList[0];
    var light_icon = `https://github.com/tutosrivegamerLQ/images-projects-srm-trg/raw/main/svg-icons-flags-cursor/${type}/${name}-l.svg`;
    var dark_icon = `https://github.com/tutosrivegamerLQ/images-projects-srm-trg/raw/main/svg-icons-flags-cursor/${type}/${name}-d.svg`;
    url_icos.push([light_icon, dark_icon]);
  });

  try {
    // desde i = 0 hasta longitud de icon -1
    for (var i = 0; i < icon.length; i++) {
      // ico[i] => ico[0], ico[1]... ico[n]
      var ico = icon[i];
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
    console.error("Error catched by SRM: " + error);
  }
}

// Opne cualquier url sin necesidad de <a>
var urlOpen = (str) => {
  var url = new URL(str);
  open(url);
};

// Cambiar Lenguage
function language(language, nameRadiosMain) {
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
  var solicitud = new Request(`files/language/${language}.json`);
  var page_title = document.querySelector("#page_title");
  var description = document.querySelector("#description");
  var whats_title = document.querySelector("#whats_title");
  var spam_download = document.querySelector("#spam_download");
  var whats_pdftoword = document.querySelector("#whats_pdftoword");
  var features = document.querySelector("#features");
  var how_use_title = document.querySelector("#how_use_title");
  var how_use = document.querySelector("#how_use");
  var limits = document.querySelector("#limits");
  var known_bugs_title = document.querySelector("#known_bugs_title");
  var known_bugs = document.querySelector("#known_bugs");
  var summary_readme_pdftoword = document.querySelector(
    "#summary_readme_pdftoword"
  );
  var summary_readme_pdf2docx = document.querySelector(
    "#summary_readme_pdf2docx"
  );
  var comments = document.querySelector("#comments");
  var autor = document.querySelector("#autor");

  try {
    // Solicitud de abrir y acceder al archivo
    fetch(solicitud)
      .then((res) => res.json())
      .then((data) => {
        page_title.innerHTML = `${data["page_title"]}`;
        description.innerHTML = `${data["description"]}`;
        whats_title.innerHTML = `${data["whats_title"]}`;
        spam_download.innerHTML = `${data["spam_download"]}`;
        whats_pdftoword.innerHTML = `${data["whats_pdftoword"]}`;
        features.innerHTML = `${data["features"]}`;
        how_use_title.innerHTML = `${data["how_use_title"]}`;
        how_use.innerHTML = `${data["how_use"]}`;
        limits.innerHTML = `${data["limits"]}`;
        known_bugs_title.innerHTML = `${data["known_bugs_title"]}`;
        known_bugs.innerHTML = `${data["known_bugs"]}`;
        summary_readme_pdftoword.innerHTML = `${data["summary_readme_pdftoword"]}`;
        summary_readme_pdf2docx.innerHTML = `${data["summary_readme_pdf2docx"]}`;
        comments.innerHTML = `${data["comments"]}`;
        autor.innerHTML = `${data["autor"]}`;
      });
  } catch (error) {
    console.error("Error en (SRM): " + error);
  }
}

function getLanMain(nameRadios) {
  var radios = document.getElementsByName(nameRadios);
  var lan;
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
  var docx2 = document.getElementsByName("lan-pdf2docx");
  var docxto = document.getElementsByName("lan-pdftoword");
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
function fetchReadmeMD(file, idHtmlObject) {
  // Agregar el contenido de readme_pdf2docx al blockquote
  const readme_pdf2docx = new Request(file);
  var containerBlockQuote = document.querySelector(`#${idHtmlObject}`);

  try {
    fetch(readme_pdf2docx)
      .then((respon) => respon.text())
      .then((content) => {
        var htmlContent = marked.marked(content);
        containerBlockQuote.innerHTML = htmlContent;
      });
  } catch (error) {
    console.error("Error en (SRM): " + error);
  }
}

function getLanpReadme(nameRadios, nameFile, idContainer, idImgLan) {
  // var select = document.querySelector(`#${idSelect}`);
  var lans = document.getElementsByName(nameRadios);
  var lan;
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
  var radios = document.getElementsByName("lan-main");
  radios.forEach((radio) => {
    radio.setAttribute("onchange", 'radiosLanWho("lan-main")');
  });
}
function lanOnChangePdfToWord() {
  var radios = document.getElementsByName("lan-pdftoword");
  radios.forEach((radio) => {
    radio.setAttribute("onchange", 'radiosLanWho("lan-pdftoword")');
  });
}
function lanOnChangePdf2Docx() {
  var radios = document.getElementsByName("lan-pdf2docx");
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
  var imgButton = document.querySelector(`#${id}`);
  imgButton.setAttribute("src", `https://github.com/tutosrivegamerLQ/images-projects-srm-trg/raw/main/svg-icons-flags-cursor/flags-svg/flag-${lan}.svg`);
}

function colorTxt(idColorSelector) {
  var colorSelector = document.querySelector(`#${idColorSelector}`);
  var body = document.body;
  colorSelector.addEventListener(
    "input",
    (event) => (body.style.cssText = `--body-color: ${event.target.value}`)
  );
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
}