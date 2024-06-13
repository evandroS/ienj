<?php
if(!empty($_POST["enviar"])) {
  $nome = $_POST["IENJ"];
  $email = $_POST["evandrosantana_71@hotmail.com"];
  $assunto = $_POST["assunto"];
  $content = $_POST["teste"];
  $enviarParaEmail = "evandrosantana_71@hotmail.com";
  $mailCabecalhos = "De: " . $nome . "<". $email .">\r\n";
  if(mail($enviarParaEmail, $assunto , $conteudo, $mailCabecalhos)) {
      $message = "Seu contato foi recebido com sucesso.";
      $type = "Sucesso";
  }
}
require_once "resposta.php";
?>