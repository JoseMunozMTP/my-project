Feature: Alerts

  Scenario: alert normal
    Given el usuario accede al portal
    When el usuario clica en el boton "Click for JS Alert"
    And el usuario clica en "Aceptar"
    Then aparece el mensaje "You successfully clicked an alert"

    @wip
  Scenario Outline: alert de 2 opciones
    Given el usuario accede al portal
    When el usuario clica en el boton "Click for JS Confirm"
    And el usuario clica en "<boton>"
    Then aparece el mensaje "<mensaje>"

      Examples:
        | boton    | mensaje             |
        | Aceptar  | You clicked: Ok     |
        | Cancelar | You clicked: Cancel |


  Scenario Outline: alert con prompt
    Given el usuario accede al portal
    When el usuario clica en el boton "Click for JS Prompt"
    And el usuario escribe "Pepe" en el campo
    And el usuario clica en "<boton>"
    Then aparece el mensaje "<mensaje>"

          Examples:
        | boton    | mensaje             |
        | Aceptar  | You entered: Pepe     |
        | Cancelar | You entered: null|