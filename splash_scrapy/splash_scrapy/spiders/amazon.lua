-- https://www.amazon.com/b?node=283155

function main(splash, args)
    assert(splash:go(args.url))
    assert(splash:wait(0.5))
    
    input_box = assert(splash:select("#twotabsearchtextbox"))
       input_box:focus()
    input_box:send_text("books")
    assert(splash:wait(0.5))
    
    button = assert(splash:select("#nav-search-submit-button"))
    button:mouse_click()
    assert(splash:wait(4))
    
    return {
      html = splash:html(),
      png = splash:png(),
    }
  end