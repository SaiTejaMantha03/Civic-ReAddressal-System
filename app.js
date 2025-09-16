// Smooth scroll for nav links
document.querySelectorAll('nav a[href^="#"]').forEach((anchor) => {
  anchor.addEventListener('click', (e) => {
    const href = anchor.getAttribute('href')
    if (!href) return
    const target = document.querySelector(href)
    if (target) {
      e.preventDefault()
      target.scrollIntoView({ behavior: 'smooth' })
    }
  })
})

// Details accordion poly UX: close others when one opens
const accordion = document.getElementById('accordion')
if (accordion) {
  accordion.addEventListener('toggle', (e) => {
    const target = e.target
    if (target.tagName === 'DETAILS' && target.open) {
      accordion.querySelectorAll('details').forEach((d) => {
        if (d !== target) d.open = false
      })
    }
  }, true)
}


