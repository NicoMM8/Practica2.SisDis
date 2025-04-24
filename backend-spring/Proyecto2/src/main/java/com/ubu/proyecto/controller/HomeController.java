package com.ubu.proyecto.controller;

import com.ubu.proyecto.service.ExternalApiService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;

@Controller
public class HomeController {

    @Autowired
    private ExternalApiService externalApiService;

    @GetMapping("/")
    public String index() {
        return "index";  // Renderiza templates/index.html
    }

    @GetMapping("/login")
    public String login() {
        return "login";  // Renderiza templates/login.html
    }

    @GetMapping("/simulate")
    public String simulateAPI(Model model) {
        try {
            // Llama a la función que invoca el API Python
            String response = externalApiService.callPythonApi();
            model.addAttribute("data", response);
        } catch(Exception e) {
            model.addAttribute("error", "Error en la conexión a la API Python: " + e.getMessage());
        }
        return "simulate";  // Renderiza templates/simulate.html
    }
}
