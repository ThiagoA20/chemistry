let expand = 1

let navbox = document.getElementsByClassName('dash-container')[0]
let viewbox = document.getElementsByClassName('views-container')[0]

let arrow = document.getElementsByClassName('arrow')[0]

let dashm = document.getElementsByClassName('dash-main')[0]
let logo = document.getElementsByClassName('tb-text')[0]

let dashbt = document.getElementsByClassName('nav-element')
let dashmain = document.getElementsByClassName('dash-element')

let text = document.getElementsByClassName('nav-text')
let img = document.getElementsByClassName('nav-image')

let inobt = document.getElementById('inorganic-bt')
let orbt = document.getElementById('organic-bt')

let selector = document.getElementsByClassName('selector')[0]
let inorganic_creator = document.getElementsByClassName('inorganic-creator')[0]
let organic_creator = document.getElementsByClassName('organic-creator')[0]
let l_arrow = document.getElementsByClassName('left-arrow')[0]
let r_arrow = document.getElementsByClassName('right-arrow')[0]

l_arrow.addEventListener('click', () => {
    inorganic_creator.style.margin = "0px 0px 0px -3100px"
    organic_creator.style.margin = "0px 0px 0px 3100px"
    selector.style.margin = "0px 0px 0px 0px"
})

r_arrow.addEventListener('click', () => {
    inorganic_creator.style.margin = "0px 0px 0px -3100px"
    organic_creator.style.margin = "0px 0px 0px 3100px"
    selector.style.margin = "0px 0px 0px 0px"
})

inobt.addEventListener('click', () => {
    inorganic_creator.style.margin = "0px 0px 0px 0px"
    organic_creator.style.margin = "0px 0px 0px 3100px"
    selector.style.margin = "0px 0px 0px 3100px"
})

orbt.addEventListener('click', () => {
    inorganic_creator.style.margin = "0px 0px 0px -3000px"
    organic_creator.style.margin = "0px 0px 0px 0px"
    selector.style.margin = "0px 0px 0px -3000px"
})

arrow.addEventListener('click', () => {
    if (expand == 0) {
        arrow.style.transform = "rotate(0deg)"
        navbox.style.width = "5%"
        viewbox.style.width = "95%"
        for (let i = 0; i < text.length; i++) {
            text[i].style.display = 'none'
            img[i].style.display = 'block'
        }
        expand = 1
    } else {
        arrow.style.transform = "rotate(180deg)"
        navbox.style.width = "15%"
        viewbox.style.width = "85%"
        for (let i = 0; i < text.length; i++) {
            text[i].style.display = 'block'
            img[i].style.display = 'none'
        }
        expand = 0
    }
})

for (let i = 0; i < dashbt.length; i++) {
    if (i == 0) {
        dashbt[i].addEventListener('click', () => {
            dashm.style.display = 'block'
            for (let e = 1; e < dashbt.length; e++) {
                if (e == i) {
                    dashmain[e].style.display = 'block'
                } else {
                    dashmain[e].style.display = 'none'
                }
            }
        })
    } else {
        dashbt[i].addEventListener('click', () => {
            dashm.style.display = 'none'
            for (let e = 0; e < dashbt.length; e++) {
                if (e == i) {
                    dashmain[e].style.display = 'block'
                } else {
                    dashmain[e].style.display = 'none'
                }
            }
        })
    }
}

let switchh = document.getElementById('switch')
let table = document.getElementById('table')
let count = 1
let ptable = document.getElementsByClassName('Periodic-table')[0]
let smodel = document.getElementsByClassName('Standard-model')[0]
let chem = document.getElementsByClassName('chem-table')[0]
let phys = document.getElementsByClassName('phys-table')[0]
let bord = document.getElementsByClassName('switch-tables')[0]

switchh.addEventListener('click', () => {
    if (count == 1) {
        table.textContent = 'Standard Model'
        ptable.style.display = 'none'
        smodel.style.display = 'block'
        chem.style.opacity = 0.5
        phys.style.opacity = 1
        count = 0
    } else {
        table.textContent = 'Periodic Table'
        ptable.style.display = 'block'
        smodel.style.display = 'none'
        chem.style.opacity = 1
        phys.style.opacity = 0.5
        count = 1
    }
})

buildPeriodicTable()

function buildPeriodicTable() {
    let ptableContainer = ptable
    let url = "http://127.0.0.1:8000/api/ptable/"

    fetch(url)
    .then((resp) => resp.json())
    .then(function(data){
        let PeriodicTable = data
        for (let i in Array.from({length: 9}, (x, i) => i)) {
            let line = `
                <div id="ptable-line-${i}" class="ptable-line">
                </div>
            `
            ptableContainer.innerHTML += line
        }

        lines = document.getElementsByClassName('ptable-line')
        let atom = 1
        let n = 0
        let nmax = 2
        let lineiterator;
        for (let i = 0; i < lines.length; i++) {
            lineiterator = lines[i]
            if (i == 7 || i == 8) {
                let space = `
                        <div class='space4'></div>
                    `
                lineiterator.innerHTML += space
            }
            while (n < nmax) {
                for (let u in PeriodicTable) {
                    if (PeriodicTable[u].Atomic_number == atom){
                        let element = `
                            <div id="data-row-${i}" class="p-element ${(PeriodicTable[u].Serie).replace(' ', '-')}">
                                <div>
                                    <span>${PeriodicTable[u].Atomic_number}</span>
                                </div>
                                <div>
                                    <span>${PeriodicTable[u].simbolo}</span>
                                </div>
                                <div>
                                    <span>${PeriodicTable[u].Name}</span>
                                </div>
                                <div>
                                    <span>${PeriodicTable[u].Atomic_mass}</span>
                                </div>
                            </div>
                        `
                        lineiterator.innerHTML += element
                    }
                }
                if (atom == 56) {
                    let space = `
                        <div class='p-element'></div>
                    `
                    lineiterator.innerHTML += space
                    nmax -= 1
                    atom += 16
                } else if (atom == 88) {
                    let space = `
                        <div class='p-element'></div>
                    `
                    lineiterator.innerHTML += space
                    atom += 16
                } else if (atom == 118) {
                    atom -= 61
                    nmax -= 2
                } else if (atom == 71) {
                    atom += 18
                } else if (atom == 103) {
                    atom += 200
                } else {
                    atom += 1
                }
                if (atom == 2) {
                    let space = `
                        <div class='space1'></div>
                    `
                    lineiterator.innerHTML += space
                } else if (atom == 5 || atom == 13) {
                    let space = `
                        <div class='space2'></div>
                    `
                    lineiterator.innerHTML += space
                }
                n += 1
            }
            n = 0
            if (i == 0) {
                nmax += 6
            } else if (i == 2) {
                nmax += 10
            } else {}
        }
    })
}
// 
// 
// 
// 
// 
// Criador de moléculas inorgânicas
// 
// 
// 
// 
// 
// nav bar
let delmolin = document.getElementById('del-in')
let savemolin = document.getElementById('save-in')
// Forma de apresentação
let lewis = document.getElementById('lewis')
let estrutural = document.getElementById('estrutural')
let molecular = document.getElementById('molecular')
let threeD = document.getElementById('3d')
// Informações
let nox_in = document.getElementById('nox-in')
let name_in = document.getElementById('name-in')
let class_in = document.getElementById('class-in')
let mass_in = document.getElementById('mass-in')
let eletrons_in = document.getElementById('eletrons-in')
let estabilidade = document.getElementById('estabilidade-in')
// molecula
let molecule_preview = document.getElementById('molecule_preview')
// .getContext('2d')
// molecule_preview.font = '38px serif'
// molecule_preview.fillStyle = 'white'
// molecule_preview.textAlign = "center"

// Atomos
let atomos_select = document.getElementById('atom-selection')

let atmbt = document.getElementsByClassName('atom-button')

AtomsSelect()

function AtomsSelect(){
    let url = "http://127.0.0.1:8000/api/ptable/"

    fetch(url)
    .then((resp) => resp.json())
    .then(function(data){
        let PeriodicTable = data
        PeriodicTable.sort(function (x, y) {
            return y.Electronegativity - x.Electronegativity
        })
        for (let i in PeriodicTable) {
            if (PeriodicTable[i].Serie == "Alkali metals" || PeriodicTable[i].Serie == "Alkaline earth metals" || PeriodicTable[i].Serie == "Transition metals" || PeriodicTable[i].Serie == "Post-transition metals" || PeriodicTable[i].Serie == "Reactive nonmetals" || PeriodicTable[i].Serie == "Metalloids") {
                let atom_element = `
                    <button class="atom-button ${(PeriodicTable[i].Serie).replace(' ', '-').replace('earth metals', 'earth-metals')}-in" id="${PeriodicTable[i].simbolo}-${PeriodicTable[i].Atomic_number}-${PeriodicTable[i].Energy_level}-${PeriodicTable[i].Electronegativity}-${PeriodicTable[i].Serie}-${PeriodicTable[i].Atomic_mass}">${PeriodicTable[i].simbolo}</button>
                `
                atomos_select.innerHTML += atom_element
            }
        }
        for (let i of atmbt) {
            i.addEventListener('click', () => {
                atomObject(i.id)
            })
        }
    })
}

var nova_molecula = true
var molecula = {}

delmolin.addEventListener('click', () => {
    molecule_preview.textContent = ""
    // .clearRect(0, 0, molecule_preview.canvas.width, molecule_preview.canvas.height)
    nox_in.textContent = ""
    name_in.textContent = ""
    class_in.textContent = ""
    mass_in.textContent = ""
    estabilidade.textContent = ""
    eletrons_in.textContent = ""
    for (i in atmbt) {
        if (atmbt[i].id != undefined){
            atmbt[i].style.border = "0.1px solid orangered"
        }
    }
    nova_molecula = true
})

function NewMol(){
    molecula = {}
    molecula["elements"] = []
    molecula["name"] = ''
    molecula["polaridade"] = false
    molecula["class"] = ''
    molecula["nox"] = 0
    molecula["carga"] = 0
    molecula["novo"] = true
    return molecula
}




// Funções Principais




// Recebe informações do atomo clicado e envia o elemento para a função de atualizar a molécula
function atomObject(atom) {
    let raw_atom_info = atom.split('-')
    
    let elemento = {};
    elemento["abreviacao"] = raw_atom_info[0]
    elemento["atomic_number"] = parseInt(raw_atom_info[1])
    elemento["camada_de_valencia"] = parseInt(raw_atom_info[2])
    elemento["eletronegatividade"] = parseFloat(raw_atom_info[3])
    elemento["Serie"] = raw_atom_info[4]
    elemento["Atomic_mass"] = parseFloat(raw_atom_info[5])
    elemento["carga"] = 0
    elemento["Quantidade"] = 1

    if (nova_molecula == true) {
        molecula = NewMol()
        atualizarMolecula(elemento)
        nova_molecula = false
        balancearLigacoes(elemento, molecula)
    } else {
        atualizarMolecula(elemento)
        balancearLigacoes(elemento, molecula)
    }
}

// Recebe o novo elemento e atualiza os parâmetros da molécula
function atualizarMolecula(elemento){
    // adicionar elementos
    if (nova_molecula == true) {
        molecula.elements.push(elemento)
    } else {
        let novo_elemento = true
        for (i in molecula.elements) {
            if (molecula.elements[i].abreviacao == elemento.abreviacao) {
                molecula.elements[i].Quantidade += 1
                novo_elemento = false
            }
        }
        if (novo_elemento == true) {
            molecula.elements.push(elemento)
        }
    }

    // Calcular NOX
    molecula = calcularNox(molecula)
    nox_in.textContent = molecula.nox

    // Definir a formula molecular
    // molecule_preview.clearRect(0, 0, molecule_preview.canvas.width, molecule_preview.canvas.height)
    // molecule_preview.fillText(`${formulaMolecular(molecula)}`, 155, 89)
    molecule_preview.textContent = ""
    for (i in molecula.elements) {
        molecule_preview.innerHTML += `<span>${molecula.elements[i].abreviacao}</span>`
        if (molecula.elements[i].Quantidade != 1) {
            molecule_preview.innerHTML += `<sub>${molecula.elements[i].Quantidade}</sub>`
        }
    }
    // molecule_preview.textContent = formulaMolecular(molecula)
    
    // Calcular a massa molecular
    mass_in.textContent = `${calcularMassa(molecula)} g/mol`

    // Definir o nome da molécula
    // name_in.textContent = nomearMolecula(molecula)

    // Definir a classe
    // class_in.textContent = definirClasse(molecula)
}




// Funções dos parâmetros das moléculas




// Atualizar as ligações, mudando as cores dos que farão ligação iônica e covalente na molécula
function balancearLigacoes(elemento, molecula){
    if (elemento.camada_de_valencia < 4) {
        molecula.carga -= elemento.camada_de_valencia
    } else if (elemento.camada_de_valencia > 4) {
        molecula.carga += elemento.camada_de_valencia
    } else {
        if (molecula.carga < 0) {
            molecula.carga += elemento.camada_de_valencia
        } else if (molecula.carga > 0) {
            molecula.carga -= elemento.camada_de_valencia
        } else {
            molecula.carga = elemento.camada_de_valencia
        }
    }
    eletrons_in.textContent = molecula.carga
    if (molecula.carga != 0) {
        estabilidade.textContent = "instável"
        estabilidade.style.color = "red"
        eletrons_in.style.color = "red"
    } else {
        estabilidade.textContent = "estável"
        estabilidade.style.color = "lime"
        eletrons_in.style.color = "lime"
    }
    for (i in atmbt) {
        if (atmbt[i].id != undefined){
            let atm = atmbt[i].id.split('-')
            let atm_number = parseInt(atm[1])
            let atm_cdv = parseInt(atm[2])

            if (atm_number == 3) {
                atmbt[i].style.border = "0.1px solid blue"
            } else if (atm_number == 4) {
                atmbt[i].style.border = "0.1px solid blue"
            } else if (atm_number == 5) {
                atmbt[i].style.border = "0.1px solid blue"
            } else if (atm_number == 7) {
                atmbt[i].style.border = "0.1px solid blue"
            } else if (atm_number == 13) {
                atmbt[i].style.border = "0.1px solid blue"
            } else if (atm_number == 15) {
                atmbt[i].style.border = "0.1px solid blue"
            } else if (atm_number == 16) {
                atmbt[i].style.border = "0.1px solid blue"
            } else if (atm_number == 17) {
                atmbt[i].style.border = "0.1px solid blue"
            } else {
                if (atm_cdv < 4) {
                    atmbt[i].style.border = "0.1px solid yellow"
                } else if (atm_cdv > 4) {
                    atmbt[i].style.border = "0.1px solid green"
                } else {
                    atmbt[i].style.border = "0.1px solid red"
                }
            }
        }
    }
    // Definir elementos que farão ligação iônica e os que farão ligação covalente com a molécula
    // elementos --> atmbt
    // mudar a cor dos elementos para tipo de ligação
    // adicionar propriedade display none as que não se ligarem
}



function formulaMolecular(molecula){
    let molecula_name = ""
    for (i in molecula.elements) {
        molecula_name += `${molecula.elements[i].abreviacao}`
        if (molecula.elements[i].Quantidade != 1){
            molecula_name += `${molecula.elements[i].Quantidade}`
        }
    }
    return molecula_name
}


function nomearMolecula(){
    // íons (cátions e ânions)
    // Ácidos:
    // Hidrácidos
    // Oxiácidos
    // Bases
    // Sais
    // Óxidos
}

function calcularNox(molecula){

    molecula.elements.sort(function (x, y){
        return x.eletronegatividade - y.eletronegatividade
    })

    let x = 0
    if (molecula.elements.length == 1 & molecula.elements[0].carga != 0) {
        x = parseInt(molecula.elements[0].carga)
    }

    molecula.nox = x

    return molecula

    // for (i in molecula.elements) {
        // qual elemento e necessidade de dar/receber eletrons
        // ordenar por eletronegatividade
        // balancear eletrons de acordo com necessidade de dar/receber eletrons
    // }
    // Substância neutra = 0
    // íon = carga
    // Substância não-neutra = carga
    // Substância simples é 0
}

function definirClasse(){
    // Ácido, Base, Sal, Óxido
}

function calcularMassa(molecula){
    let mm = 0
    for (i in molecula.elements){
        mm += molecula.elements[i].Atomic_mass * molecula.elements[i].Quantidade
    }
    return mm.toFixed(3)
}