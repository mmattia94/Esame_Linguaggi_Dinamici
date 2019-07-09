--
-- USO: mysql -p < create_tables_campionato_calcio.sql
--

DROP DATABASE IF EXISTS esame;

CREATE database esame;
USE esame;

CREATE TABLE `campionato_calcio_campionato` (
       `id` INT(11) NOT NULL,
       `nome` VARCHAR(16) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `campionato_calcio_squadra` (
       `id` INT(11) NOT NULL,
       `nome` VARCHAR(16) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;			

CREATE TABLE `campionato_calcio_calendario` (
       `id` INT(11) NOT NULL,
       `campionato` int(11) NOT NULL,
       `giornata` int(2) NOT NULL,
       `AR` CHAR(1) NOT NULL,
       `data` VARCHAR(10) NOT NULL,
       `locali` int(11) NOT NULL,
       `ospiti` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `campionato_calcio_risultati` (
       `id` INT(11) NOT NULL,
       `partita` int(11) NOT NULL,
       `retiLocali` int(2) NOT NULL,
       `retiOspiti` int(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE `campionato_calcio_opzioni` (
       `id` INT(11) NOT NULL,
       `nome` VARCHAR(50) NOT NULL,
       `code` VARCHAR(11) NOT NULL,
       `icon` VARCHAR(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

ALTER TABLE `campionato_calcio_campionato`
      ADD PRIMARY KEY (`id`);

ALTER TABLE `campionato_calcio_squadra`
      ADD PRIMARY KEY (`id`);

ALTER TABLE `campionato_calcio_calendario`
      ADD PRIMARY KEY (`id`);

ALTER TABLE `campionato_calcio_risultati`
      ADD PRIMARY KEY (`id`);
	  
ALTER TABLE `campionato_calcio_opzioni`
ADD PRIMARY KEY (`id`);

ALTER TABLE `campionato_calcio_campionato`
      MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;

ALTER TABLE `Squadre`
      MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;

ALTER TABLE `campionato_calcio_calendario`
      MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;

ALTER TABLE `Risultati`
      MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1;

ALTER TABLE `Calendario`
      ADD FOREIGN KEY (campionato) REFERENCES Campionati(id);

ALTER TABLE `campionato_calcio_calendario`
      ADD FOREIGN KEY (locali) REFERENCES Squadre(id);

ALTER TABLE `campionato_calcio_calendario`
      ADD FOREIGN KEY (ospiti) REFERENCES Squadre(id);

ALTER TABLE `Risultati`
      ADD FOREIGN KEY (partita) REFERENCES Calendario(id);
