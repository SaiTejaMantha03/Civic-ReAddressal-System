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
  accordion.addEventListener('click', (e) => {
    if (e.target.tagName === 'SUMMARY') {
      const details = e.target.parentElement
      setTimeout(() => {
        if (details.open) {
          accordion.querySelectorAll('details').forEach((d) => {
            if (d !== details) d.open = false
          })
        }
      }, 0)
    }
  })
}


